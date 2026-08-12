import joblib
import os
import numpy as np
from sklearn.ensemble import IsolationForest

# Make sure the models directory exists
os.makedirs('models', exist_ok=True)

# 1. Generate normal-looking IoT data (Temp around 30C, Voltage around 3.3V)
normal_data = np.random.normal(loc=[30.0, 3.3], scale=[3.0, 0.15], size=(200, 2))

# 2. Train the model using your current scikit-learn version
clf = IsolationForest(contamination=0.05, random_state=42)
clf.fit(normal_data)

# 3. Save it (this will overwrite the old one)
joblib.dump(clf, 'models/anomaly_model.pkl')
print("Model retrained successfully for your current environment!")