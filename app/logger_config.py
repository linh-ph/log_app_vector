import logging
import json
import requests
from pythonjsonlogger import jsonlogger

VECTOR_ENDPOINT = "http://localhost:8080"  # Vector nhận log qua HTTP

# Cấu hình logger
logger = logging.getLogger("fastapi-logger")
logger.setLevel(logging.INFO)

# Ghi log vào file (tuỳ chọn)
file_handler = logging.FileHandler("app.log")
formatter = jsonlogger.JsonFormatter("%(timestamp)s %(levelname)s %(message)s %(project)s %(function)s %(status)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def send_log(project, function, status, message):
    """Gửi log đến Vector"""
    log_data = {
        "timestamp": "2024-03-05T12:34:56Z",
        "project": project,
        "function": function,
        "status": status,
        "message": message
    }
    try:
        response = requests.post(VECTOR_ENDPOINT, json=log_data, timeout=2)
        print("response", response)
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to send log: {e}")
