# Chọn image chính thức của Python
FROM python:3.10-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép requirements.txt vào container
COPY requirements.txt .

# Cài đặt tất cả các thư viện cần thiết từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn của ứng dụng vào container
COPY ./app /app

# Cấu hình FastAPI để chạy với Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
