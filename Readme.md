 # Đồ Án: API xử lý văn bản tiếng Việt

## Mô Tả

Với đề tài này, các bạn hãy tìm hiểu và cài đặt các API xử lý văn bản tiếng Việt (tiền xử lý, chuẩn hóa encoding, dấu câu, dấu thanh, loại bỏ các ký tự đặc biệt/dư thừa/mã HTML..., tách câu). API có thể thực hiện riêng rẽ hoặc đồng thời nhiều thao tác cùng lúc.

---

## Cài Đặt Môi Trường

Để bắt đầu, bạn cần cài đặt môi trường ảo để quản lý các phụ thuộc. Dưới đây là hướng dẫn để cài đặt môi trường ảo:

1. **Cài đặt Python (Nếu chưa có):**
   - Tải Python từ trang chính thức [python.org](https://www.python.org/downloads/) và cài đặt.

2. **Tạo môi trường ảo:**
   ```bash
   python -m venv env
3. **Kích hoạt môi trường ảo**
   ```bash
    # Trên Windows
    env\Scripts\activate
    # Trên macOS/Linux
    source env/bin/activate
4. **Cài đặt requirements.txt**
    - Sau khi kích hoạt môi trường ảo, cài đặt các gói phụ thuộc được liệt kê trong requirements.txt
    ```bash
    pip install -r requirements.txt
## Khởi chạy chương trình
1. **Để khởi động API**
    - Chạy file api.py trong nền: Tại thư mục NLP-Project, sử dụng lệnh sau:
    ```bash
    python src/api/api.py
2. **Để chạy giao diện người dùng Streamlit**
    - Tại thư mục NLP-Project, mở một terminal mới và sử dụng lệnh sau
    ```bash
    streamlit run src/gui/gui.py
Ứng dụng Streamlit sẽ mở ra trên trình duyệt web của bạn.

---

## Các tài liệu liên quan:
[Python Virtual Environments](https://docs.python.org/3/library/venv.html)

[Streamlit Documentation](https://docs.streamlit.io/)

---
## Liên hệ:
Nếu bạn gặp vấn đề hoặc có câu hỏi, vui lòng liên hệ với nhóm phát triển qua email: [hoapham.pth@gmail.com](hoapham.pth@gmail.com)

---
