# 🛡️ CyberScope-AI: IoT Security Information & Event Management (SIEM)

CyberScope-AI is a lightweight, machine-learning-powered SIEM platform designed specifically for monitoring IoT edge networks. It ingests real-time telemetry from edge nodes (like ESP32 sensors), detects hardware anomalies or security threats using unsupervised machine learning, and visualizes the data in a secure, enterprise-grade Security Operations Center (SOC) dashboard.

## 📸 Interface Showcase

**1. SOC Dashboard & Real-Time Analytics**
![Dashboard](assets/Screenshot%202026-08-11%20230752.png)

**2. Incident Management & AI Threat Classification**
![Incidents Management](assets/Screenshot%202026-08-11%20230811.png)

**3. ML Benchmarking & Security Analytics**
![Security Analytics](assets/Screenshot%202026-08-11%20230825.png)

**4. Deep Log Analyzer**
![Log Analyzer](assets/Screenshot%202026-08-11%20230717.png)

*(Note: If the screenshots appear out of order, you can simply swap the filenames in the markdown links above!)*

## ✨ Key Features

*   **Unsupervised Machine Learning:** Utilizes `scikit-learn` (Isolation Forest) to establish operational baselines and detect zero-day thermal/power anomalies without relying on static thresholds.
*   **Secure SOC Dashboard:** A responsive, dark-mode web interface built with Flask and styled with modern glassmorphism CSS. Protected by `Flask-Login` session management and password hashing.
*   **Real-Time Analytics:** Integrates `Chart.js` for dynamic visualization of traffic distributions and temperature volatility trackers.
*   **Automated PDF Compliance Reporting:** Generates downloadable, audit-ready PDF incident reports via the `ReportLab` engine.
*   **IoT Edge Simulator:** Includes a Python-based ESP32 mock simulator (`mock_esp32.py`) to stream randomized telemetry and inject realistic hardware threats into the API.
*   **Automated Testing:** Fully verified backend logic and ML models using a comprehensive `pytest` testing suite.

## 🛠️ Technology Stack

*   **Backend:** Python 3, Flask, SQLite3, Werkzeug (Security)
*   **Machine Learning:** scikit-learn, NumPy, Joblib
*   **Frontend:** HTML5, CSS3, JavaScript, Chart.js
*   **Testing & Tooling:** Pytest, ReportLab (PDFs), Batch Scripting

## 📂 Project Structure

```text
├── app.py                  # Main Flask application and API routing
├── start_cyberscope.bat    # Windows launcher for automated startup
├── requirements.txt        # Python dependency list
├── database/
│   └── db_setup.py         # SQLite schema initialization
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
