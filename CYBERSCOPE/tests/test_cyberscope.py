import pytest
import json
import sys
import os

# Ensure the tests can find your main app files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from utils.detector import detect_anomaly

@pytest.fixture
def client():
    """Sets up a mock Flask server for testing the API."""
    app.config['TESTING'] = True
    # Ensure the test environment has a mock API key
    app.config['API_KEY'] = 'test_secure_key'
    with app.test_client() as client:
        yield client

# --- 1. Machine Learning Logic Tests ---
def test_ml_detector_normal():
    """Test that the ML model correctly identifies safe operational baselines."""
    payload = {'temperature': 30.5, 'voltage': 3.3}
    is_anomaly, reason = detect_anomaly(payload)
    
    # Assert that it does NOT flag normal room-temperature data
    assert is_anomaly is False
    assert reason == "Normal"

def test_ml_detector_extreme_anomaly():
    """Test that the ML model correctly catches severe hardware spikes."""
    payload = {'temperature': 95.0, 'voltage': 5.5}
    is_anomaly, reason = detect_anomaly(payload)
    
    # Assert that it catches the fire hazard and tags it as a threat
    assert is_anomaly is True
    assert "CRITICAL" in reason

# --- 2. REST API Endpoint Tests ---
def test_api_ingest_normal(client):
    """Test that the server accepts normal API data and returns HTTP 200 (OK)."""
    payload = {
        "sensor_id": "TEST-ESP32",
        "temperature": 29.5,
        "voltage": 3.29
    }
    
    # Pass the API key in the headers
    headers = {"X-API-Key": app.config['API_KEY']}
    response = client.post('/api/ingest', json=payload, headers=headers)
    
    assert response.status_code == 200
    assert response.get_json()['status'] == 'ok'

def test_api_ingest_anomaly_logging(client):
    """Test that the server correctly logs anomalies to the database and returns HTTP 201 (Created)."""
    payload = {
        "sensor_id": "TEST-ESP32",
        "temperature": 92.0,
        "voltage": 5.8
    }
    
    # Pass the API key in the headers
    headers = {"X-API-Key": app.config['API_KEY']}
    response = client.post('/api/ingest', json=payload, headers=headers)
    
    assert response.status_code == 201
    assert response.get_json()['status'] == 'anomaly_logged'