import os

# Define the contents of the three test CSV files
csv_files = {
    "test_mixed.csv": (
        "sensor_id,temperature,voltage,timestamp\n"
        "ESP32-01,30.5,3.31,2026-08-11T16:00:00\n"
        "ESP32-01,31.1,3.29,2026-08-11T16:01:00\n"
        "ESP32-01,30.8,3.30,2026-08-11T16:02:00\n"
        "ESP32-01,88.4,5.40,2026-08-11T16:03:00\n"
        "ESP32-01,92.1,5.65,2026-08-11T16:04:00\n"
        "ESP32-01,31.0,3.32,2026-08-11T16:05:00\n"
        "ESP32-01,29.9,3.28,2026-08-11T16:06:00\n"
    ),
    "test_clean.csv": (
        "sensor_id,temperature,voltage,timestamp\n"
        "ESP32-02,29.5,3.30,2026-08-11T17:00:00\n"
        "ESP32-02,29.8,3.31,2026-08-11T17:01:00\n"
        "ESP32-02,30.2,3.30,2026-08-11T17:02:00\n"
        "ESP32-02,30.0,3.29,2026-08-11T17:03:00\n"
        "ESP32-02,29.7,3.28,2026-08-11T17:04:00\n"
    ),
    "test_invalid.csv": (
        "SensorID,Temperature,Voltage,Time\n"
        "ESP32-03,30.5,3.31,2026-08-11T18:00:00\n"
        "ESP32-03,95.0,5.80,2026-08-11T18:01:00\n"
    )
}

# Generate the files
for filename, content in csv_files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Successfully created: {filename}")