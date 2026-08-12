# CyberScope-AI: IoT Security Information & Event Management (SIEM)

CyberScope-AI is a lightweight, machine-learning-powered SIEM platform designed specifically for monitoring IoT edge networks. It ingests real-time telemetry from edge nodes (like ESP32 sensors), detects hardware anomalies or security threats using unsupervised machine learning, and visualizes the data in a secure, enterprise-grade Security Operations Center (SOC) dashboard.

## Key Features

* **Unsupervised Machine Learning:** Utilizes `scikit-learn` (Isolation Forest) to establish operational baselines and detect zero-day thermal/power anomalies without relying on static thresholds.
* **API Key Security & Environment Protection:** Ingestion endpoints (`/api/ingest`) are secured via `X-API-Key` header authentication, with secrets managed dynamically using `python-dotenv`.
* **Secure SOC Dashboard:** A responsive, dark-mode web interface built with Flask and styled with modern glassmorphism CSS. Protected by `Flask-Login` session management and password hashing.
* **Real-Time Analytics:** Integrates `Chart.js` for dynamic visualization of traffic distributions and temperature volatility trackers.
* **Automated In-Memory PDF Compliance Reporting:** Generates downloadable, audit-ready PDF incident reports via the `ReportLab` engine directly in memory without leaving temporary disk artifacts.
* **IoT Edge Simulator:** Includes a Python-based ESP32 mock simulator (`mock_esp32.py`) to stream randomized telemetry and inject realistic hardware threats into the API using secure header tokens.
* **Automated Testing:** Fully verified backend logic, API authentication, and ML models using a comprehensive `pytest` testing suite.

## Technology Stack

* **Backend:** Python 3, Flask, SQLite3, Werkzeug (Security), python-dotenv
* **Machine Learning:** scikit-learn, NumPy, Joblib
* **Frontend:** HTML5, CSS3, JavaScript, Chart.js
* **Testing & Tooling:** Pytest, ReportLab (PDFs), Batch Scripting

## Project Structure

```text
├── app.py                  # Main Flask application and API routing
├── benchmark.py            # ML algorithm benchmarking script
├── benchmark_results.json  # Benchmark output data for analytics
├── generate_tests.py       # Helper script to create test datasets
├── retrain.py              # Script to retrain the ML anomaly model
├── start_cyberscope.bat    # Windows launcher for automated startup
├── requirements.txt        # Python dependency list
├── .env                    # Hidden environment variables (Secrets)
├── database/
│   ├── db_setup.py         # SQLite schema initialization
│   └── cyberscope.db       # Database storage file
├── models/
│   └── anomaly_model.pkl   # Pre-trained ML baseline model
├── sim/
│   └── mock_esp32.py       # IoT edge sensor simulator
├── tests/
│   └── test_cyberscope.py  # Pytest automated test suite
├── utils/
│   ├── detector.py         # ML heuristics and classification logic
│   ├── parser.py           # IoT payload sanitization
│   └── pdf_generator.py    # ReportLab PDF creation logic
├── static/css/             # Stylesheets (cyberscope.css)
└── templates/              # HTML Views (dashboard, incidents, analyzer)