import requests
import json
import streamlit as st
from docx import Document


base_url = "http://0.0.0.0:8000/"
path_url = "api/v1/pre-processing"
headers = {"Content-Type": "application/json"}

def call_api(text,
            clean_html=True,
            clean_special_char=True,
            clean_extra_whitespace=True,
            chuan_hoa_unicode_NFC_action=True,
            chuan_hoa_unicode_NFD_action=True,
            chuan_hoa_chu_thuong= True,
            chuan_hoa_dau_thanh=True,
            chuan_hoa_dau_cau=True,
             split_word_pyvi=True,
             split_sent=True,
             remove_sw=True
             ):
    param = {
        "text": text,
        "clean_html": clean_html,
        "clean_special_char": clean_special_char,
        "clean_extra_whitespace": clean_extra_whitespace,
        "chuan_hoa_unicode_NFC_action": chuan_hoa_unicode_NFC_action,
        "chuan_hoa_unicode_NFD_action": chuan_hoa_unicode_NFD_action,
        "chuan_hoa_chu_thuong": chuan_hoa_chu_thuong,
        "chuan_hoa_dau_thanh": chuan_hoa_dau_thanh,
        "chuan_hoa_dau_cau": chuan_hoa_dau_cau,
        "split_word_pyvi": split_word_pyvi,
        "split_sent": split_sent,
        "remove_sw": remove_sw,

    }
    url = base_url + path_url
    rsp = requests.get(url=url, params=param, headers=headers)
    data = json.loads(rsp.text)["data"]
    return data

# Hàm để đọc file text
def read_txt(file):
    return file.read().decode('utf-8')

# Hàm để đọc file Word
def read_docx(file):
    doc = Document(file)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def gui():
    st.title("ĐỒ ÁN XỬ LÝ VĂN BẢN TIẾNG VIỆT")
    text = ""
    # Cho người dùng chọn phương thức nhập liệu
    option = st.selectbox("Chọn phương thức nhập liệu:", ("Tải lên file", "Nhập văn bản trực tiếp"))
    if option == "Tải lên file":
        # Tải file lên (chỉ chấp nhận .txt và .docx)
        uploaded_file = st.file_uploader("Chọn file văn bản txt hoặc Word", type=["txt", "docx"])

        if uploaded_file is not None:
            # Xử lý file dựa trên loại file
            if uploaded_file.name.endswith(".txt"):
                text = read_txt(uploaded_file)
                # st.subheader("Nội dung file .txt")
            elif uploaded_file.name.endswith(".docx"):
                text = read_docx(uploaded_file)
    
    elif option == "Nhập văn bản trực tiếp":
        # Cho phép người dùng nhập văn bản trực tiếp
        text = st.text_input("Nhập vào đoạn văn bản cần xử lý:")
    # # Tạo giao diện tải file lên
    # st.title("Tải lên và đọc nội dung file")
    # text = st.text_input("Nhập vào đoạn văn bản cần xử lý:")
    st.write("Lựa chọn các tác vụ bạn mong muốn:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<p style='color: blue;'>Các tác vụ làm sạch dữ liệu</p>", unsafe_allow_html=True)
        clean_html = st.checkbox("Xoá mã HTML")
        clean_special_char = st.checkbox("Xoá các kí tự đặc biệt")
        clean_extra_whitespace = st.checkbox("Xoá các khoảng trắng thừa")
        remove_sw = st.checkbox("Loại bỏ stopwords")
    with col2:
        st.markdown("<p style='color: blue;'>Các tác vụ chuẩn hoá dữ liệu</p>", unsafe_allow_html=True)
        chuan_hoa_unicode_NFC_action = st.checkbox("Chuẩn hoá unicode thành dựng sẵn")
        chuan_hoa_unicode_NFD_action = st.checkbox("Chuẩn hoá unicode thành tổ hợp")
        chuan_hoa_chu_thuong = st.checkbox("Chuẩn hoá về chữ thường")
        chuan_hoa_dau_thanh = st.checkbox("Chuẩn hoá dấu thanh")
        chuan_hoa_dau_cau = st.checkbox("Chuẩn hoá dấu câu")
    with col3:
        st.markdown("<p style='color: blue;'>Các tác vụ tách dữ liệu</p>", unsafe_allow_html=True)
        split_sent = st.checkbox("Tách câu")
        split_word_pyvi = st.checkbox("Tách từ")
        
    # Nút Start
    if st.button('Xử lý'):
        data = call_api(text=text,
                        clean_html=clean_html,
                        clean_special_char=clean_special_char,
                        clean_extra_whitespace=clean_extra_whitespace,
                        chuan_hoa_unicode_NFC_action=chuan_hoa_unicode_NFC_action,
                        chuan_hoa_unicode_NFD_action=chuan_hoa_unicode_NFD_action,
                        chuan_hoa_chu_thuong=chuan_hoa_chu_thuong,
                        chuan_hoa_dau_thanh=chuan_hoa_dau_thanh,
                        chuan_hoa_dau_cau= chuan_hoa_dau_cau,
                        split_word_pyvi=split_word_pyvi,
                        split_sent=split_sent,
                        remove_sw=remove_sw)
        # st.write("Văn bản sau khi được xử lý: ")
        with st.container():
            st.header("Văn bản sau khi được xử lý: ")
            for i in data:
                st.write(i)
    else:
        st.write('Hãy nhấn nút Xử lý để bắt đầu')


if __name__ == "__main__":
    text = f"Cộng hoàaa aa..."
    call_api(text)
    gui()
