import numpy as np
import time
import json
import os
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor

print("Generating extreme stealth anomalies (Hard Mode)...")

# 1. Generate Dataset - EXTREME STEALTH MODE
# Normal data: tight cluster around 30°C and 3.3V
normal_data = np.random.normal(loc=[30.0, 3.3], scale=[1.5, 0.1], size=(10000, 2))

# Stealth Anomalies: Barely drifting above normal (e.g., 33.5°C). 
# This forces the models to make extremely tough borderline decisions.
anomaly_data = np.random.normal(loc=[33.5, 3.5], scale=[1.0, 0.1], size=(500, 2))

X_test = np.vstack([normal_data, anomaly_data])
y_true = np.append(np.ones(10000), np.full(500, -1))

# 2. Define models with slightly different sensitivities to force visual variation
models = {
    "Isolation Forest": IsolationForest(contamination=0.04, random_state=42),
    "One-Class SVM": OneClassSVM(nu=0.03, kernel="rbf", gamma=0.1),
    "Local Outlier Factor": LocalOutlierFactor(novelty=True, contamination=0.05)
}

# 3. Train and collect results
results = {}
for name, clf in models.items():
    start_time = time.time()
    
    # Train the model
    clf.fit(normal_data)
    
    # Predict on the test set
    y_pred = clf.predict(X_test)
    end_time = time.time()
    
    # Calculate metrics
    correct_anomalies = int(np.sum((y_pred == -1) & (y_true == -1)))
    false_positives = int(np.sum((y_pred == -1) & (y_true == 1)))
    
    # Calculate exact percentage
    detection_rate = round((correct_anomalies / 500) * 100, 2)
    
    results[name] = {
        "detection_rate": detection_rate,
        "false_positives": false_positives,
        "time_taken": round(end_time - start_time, 4)
    }
    
    # Print it to the terminal so you can verify it worked before checking the UI
    print(f"[{name}] Detection Rate: {detection_rate}%")

# 4. Export to JSON for the Flask app to read
with open("benchmark_results.json", "w") as f:
    json.dump(results, f)

print("\nBenchmark complete! Data exported to benchmark_results.json.")