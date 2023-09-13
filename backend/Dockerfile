# Sử dụng image chứa Python 3.9
FROM python:3.9

# Thiết lập thư mục làm việc của ứng dụng
WORKDIR /app/backend

# Sao chép các tệp ứng dụng vào thư mục làm việc của Docker
COPY . /app

# Cài đặt các gói phụ thuộc từ tệp requirements.txt (nếu có)
RUN pip install --no-cache-dir -r requirements.txt

# Expose cổng mà ứng dụng của bạn chạy trên (thay đổi thành cổng thực tế)
EXPOSE 5000

# Chạy ứng dụng Python của bạn
CMD ["python", "app.py"]
