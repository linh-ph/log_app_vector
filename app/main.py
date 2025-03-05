from fastapi import FastAPI
from logger_config import logger, send_log
from clickhouse_driver import Client

client = Client(
    host='clickhouse',
    port=9000,
    user='admin',
    password='admin123',
    database='logs_db'
)

app = FastAPI()

@app.on_event("startup")
def create_table():
    create_table_query = """
        CREATE TABLE IF NOT EXISTS logs_db.logs (
            timestamp DateTime DEFAULT now(),
            project String,
            function String,
            status String,
            message String
        ) ENGINE = MergeTree()
        PARTITION BY project
        ORDER BY (timestamp, function, status);
    """

    # Thực thi truy vấn
    client.execute(create_table_query)

    # print("Bảng logs đã được tạo thành công!")

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
    send_log("log_status", status, f"Received status: {status}")
    return {"status": status}

@app.get("/logs")
def log_message():
    select_query = "SELECT * FROM logs"
    rows = client.execute(select_query)

    for row in rows:
        print(row)

@app.get("/log_demo")
def create():
    insert_query = """
    INSERT INTO logs_db.logs (project, function, status, message) VALUES
    ('iot-system', 'device_processing', 'info', 'Processing data successfully'),
    ('iot-system', 'sensor_reading', 'error', 'Sensor timeout error'),
    ('iot-system', 'database_save', 'warning', 'Slow database response');
    """

    client.execute(insert_query)
    return {"message": "Log data inserted successfully"}