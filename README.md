# Format data trước khi gửi dữ liệu qua sink
>Vì data gửi qua format:
"{"accept":"/","accept-encoding":"gzip, deflate","connection":"keep-alive","content-length":"100","content-type":"application/json","host":"vector:8686","message":"{"project": "iot-system", "function": "root", "status": "info", "message": "Root endpoint accessed"}","path":"/","source_type":"http_server","timestamp":"2025-03-06T08:49:56.648474607Z","user-agent":"python-requests/2.32.3"}", khi gửi qua clickhouse gặp lỗi 400.

# Sử dụng Transforms
> Sử dụng Vector Remap Language (VRL) để phân tích trường `message` từ dữ liệu đầu vào.
sinks.print và sinks.clickhouse bây giờ sử dụng dữ liệu đã được chuyển đổi từ transform parse_message.

# Cấu trúc của script . = parse_json!(.message) trong VRL
- "." Đây là ký hiệu đại diện cho toàn bộ sự kiện hiện tại.
- parse_json!: Hàm này phân tích một chuỗi JSON và chuyển đổi nó thành một đối tượng JSON.
- .message: Đường dẫn đến trường `message` trong sự kiện hiện tại.
- Khi script này được thực thi, hàm parse_json!(.message) sẽ phân tích chuỗi JSON trong trường `message` và chuyển đổi nó thành một đối tượng JSON. Kết quả của quá trình này sẽ được gán lại cho toàn bộ sự kiện (.), nghĩa là sự kiện hiện tại sẽ được thay thế bằng đối tượng JSON đã phân tích.

**Ví dụ, nếu dữ liệu đầu vào ban đầu là:**
```json
{
  "accept": "*/*",
  "accept-encoding": "gzip, deflate",
  "connection": "keep-alive",
  "content-length": "100",
  "content-type": "application/json",
  "host": "vector:8686",
  "message": "{\"project\": \"iot-system\", \"function\": \"root\", \"status\": \"info\", \"message\": \"Root endpoint accessed\"}",
  "path": "/",
  "source_type": "http_server",
  "timestamp": "2025-03-06T08:49:56.648474607Z",
  "user-agent": "python-requests/2.32.3"
}
```

**Sau khi script . = parse_json!(.message) được thực thi, sự kiện sẽ trở thành:**
```json
{
  "project": "iot-system",
  "function": "root",
  "status": "info",
  "message": "Root endpoint accessed"
}
```