from clickhouse_driver import Client

# Kết nối đến ClickHouse
client = Client(
    host='clickhouse',
    port=9000,
    user='admin',
    password='admin123',
    database='logs_db'
)

# Truy vấn tạo bảng logs
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

print("Bảng logs đã được tạo thành công!")
