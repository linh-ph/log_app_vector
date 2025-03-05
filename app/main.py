from fastapi import FastAPI
from app.logger import logger, send_log

app = FastAPI()

@app.get("/")
def read_root():
    send_log("iot-system", "root", "info", "Root endpoint accessed")
    return {"message": "Hello, FastAPI with Vector and ClickHouse!"}

@app.get("/error")
def trigger_error():
    try:
        1 / 0  # Lỗi chia cho 0
    except ZeroDivisionError as e:
        send_log("iot-system", "trigger_error", "error", f"Error occurred: {str(e)}")
        return {"error": "Something went wrong"}

@app.get("/status/{status}")
def log_status(status: str):
    send_log("iot-system", "log_status", status, f"Received status: {status}")
    return {"status": status}
