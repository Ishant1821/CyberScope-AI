import time
import random
import requests
import datetime
import os
from dotenv import load_dotenv

# Load the API key from the .env file in the parent directory
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

URL = "http://localhost:5000/api/ingest"
API_KEY = os.environ.get('CYBERSCOPE_API_KEY', 'esp32_secure_key_2026') 

def generate_data():
    if random.random() > 0.85:
        # Generate anomalous data
        temp = random.uniform(70.0, 100.0)
        voltage = random.uniform(4.5, 6.0)
    else:
        # Generate normal data
        temp = random.uniform(25.0, 35.0)
        voltage = random.uniform(3.1, 3.5)
        
    return {
        "sensor_id": "ESP32-01",
        "temperature": round(temp, 2),
        "voltage": round(voltage, 2),
        "timestamp": datetime.datetime.now().isoformat()
    }

def run_sim():
    print("Starting ESP32 Simulator... Press Ctrl+C to stop.")
    
    # Attach the API key to the request headers
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": API_KEY
    }
    
    while True:
        data = generate_data()
        try:
            # Pass the headers along with the POST request
            response = requests.post(URL, json=data, headers=headers)
            
            if response.status_code == 401:
                print("CRITICAL ERROR: Unauthorized! Check your API key.")
                break
                
            print(f"Sent: Temp={data['temperature']}C, Volt={data['voltage']}V | Status: {response.status_code}")
        except Exception as e:
            print(f"Connection failed. Is the Flask app running?")
            
        time.sleep(2)

if __name__ == "__main__":
    run_sim()