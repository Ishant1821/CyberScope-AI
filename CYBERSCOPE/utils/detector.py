import joblib
import os
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models/anomaly_model.pkl')

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def generate_insight(temp, volt):
    """Generates a human-readable threat report based on telemetry context."""
    if temp > 90 and volt > 5.0:
        return f"CRITICAL: Simultaneous thermal ({temp}°C) and power ({volt}V) surge. High risk of hardware short-circuit. Immediate shutdown recommended."
    elif temp > 90:
        return f"WARNING: Severe thermal anomaly ({temp}°C). Voltage is stable, suggesting an external heat source or cooling system failure."
    elif volt > 5.0:
        return f"WARNING: Overvoltage detected ({volt}V). Temperature is stable, pointing to a potential power supply malfunction."
    else:
        return "Minor variance detected by ML model. Deviations are outside normal boundaries but below critical hardware thresholds. Monitor for developing trends."

def detect_anomaly(data):
    temp = data['temperature']
    volt = data['voltage']
    
    # Fallback if the model fails to load
    if model is None:
        if temp > 80 or volt > 5.0:
            return True, generate_insight(temp, volt)
        return False, "Normal"
    
    # ML Prediction
    features = np.array([[temp, volt]])
    prediction = model.predict(features)
    
    if prediction[0] == -1:
        # If the ML model flags an anomaly, generate the detailed report
        insight = generate_insight(temp, volt)
        return True, insight
        
    return False, "Normal"