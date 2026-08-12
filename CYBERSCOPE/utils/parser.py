def parse_esp32_payload(payload):
    return {
        'sensor_id': payload.get('sensor_id', 'unknown'),
        'temperature': float(payload.get('temperature', 0.0)),
        'voltage': float(payload.get('voltage', 0.0)),
        'timestamp': payload.get('timestamp')
    }
