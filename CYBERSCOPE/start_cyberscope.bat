@echo off
title CyberScope-AI Launcher
color 0B

echo ===================================================
echo      CyberScope-AI SOC Platform Initialization
echo ===================================================
echo.

echo [1/4] Running ML Benchmark to update analytics data...
python benchmark.py
echo.

echo [2/4] Starting the Flask SIEM Server...
:: Opens a new terminal window just for the server
start "CyberScope-AI Server" cmd /k "python app.py"

echo [3/4] Starting the ESP32 IoT Edge Simulator...
:: Opens a new terminal window just for the simulator
start "ESP32 Simulator" cmd /k "python sim/mock_esp32.py"

echo [4/4] Launching the SOC Dashboard...
:: Waits 3 seconds to ensure the server is fully running before opening the browser
timeout /t 3 /nobreak > NUL
start http://127.0.0.1:5000

echo.
echo ===================================================
echo SUCCESS: All systems are online!
echo You can close this launcher window safely.
echo ===================================================
pause