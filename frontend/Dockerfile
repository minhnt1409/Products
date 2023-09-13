# Sử dụng image chứa Node.js để xây dựng frontend
FROM node:14-alpine
# Thiết lập thư mục làm việc của ứng dụng
WORKDIR /app/frontend
# Sao chép các tệp ứng dụng vào thư mục làm việc của Docker
COPY package*.json ./
# cài đặt môi trường
RUN npm install
# sao chép toàn bộ từ local lên  Docker image 
COPY . .
# Expose cổng mà ứng dụng của bạn chạy trên (thay đổi thành cổng thực tế)
EXPOSE 3000
# chạy ứng dụng
CMD ["npm", "start"]
