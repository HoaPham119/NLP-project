import requests
import json
import streamlit as st

base_url = "http://0.0.0.0:8000/"
path_url = "api/v1/pre-processing"
headers = {"Content-Type": "application/json"}


def call_api(text,
            clean_html=True,
            clean_special_char=True,
            clean_extra_whitespace=True,
            chuan_hoa_unicode_action=True,
            chuan_hoa_chu_thuong= True,
            chuan_hoa_dau_thanh=True,
            chuan_hoa_dau_cau=True,
             split_word=True,
             split_sent=True,
             remove_sw=True
             ):
    param = {
        "text": text,
        "clean_html": clean_html,
        "clean_special_char": clean_special_char,
        "clean_extra_whitespace": clean_extra_whitespace,
        "chuan_hoa_unicode_action": chuan_hoa_unicode_action,
        "chuan_hoa_chu_thuong": chuan_hoa_chu_thuong,
        "chuan_hoa_dau_thanh": chuan_hoa_dau_thanh,
        "chuan_hoa_dau_cau": chuan_hoa_dau_cau,
        "split_word": split_word,
        "split_sent": split_sent,
        "remove_sw": remove_sw,

    }
    url = base_url + path_url
    rsp = requests.get(url=url, params=param, headers=headers)
    data = json.loads(rsp.text)["data"]
    return data


def gui():
    st.title("ĐỒ ÁN XỬ LÝ VĂN BẢN TIẾNG VIỆT")

    text = st.text_input("Nhập vào đoạn văn bản cần xử lý:")
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
        chuan_hoa_unicode_action = st.checkbox("Chuẩn hoá unicode")
        chuan_hoa_chu_thuong = st.checkbox("Chuẩn hoá về chữ thường")
        chuan_hoa_dau_thanh = st.checkbox("Chuẩn hoá dấu thanh")
        chuan_hoa_dau_cau = st.checkbox("Chuẩn hoá dấu câu")
    with col3:
        st.markdown("<p style='color: blue;'>Các tác vụ tách dữ liệu</p>", unsafe_allow_html=True)
        split_word = st.checkbox("Tách từ")
        split_sent = st.checkbox("Tách câu")
    # Nút Start
    if st.button('Xử lý'):
        data = call_api(text=text,
                        clean_html=clean_html,
                        clean_special_char=clean_special_char,
                        clean_extra_whitespace=clean_extra_whitespace,
                        chuan_hoa_unicode_action=chuan_hoa_unicode_action,
                        chuan_hoa_chu_thuong=chuan_hoa_chu_thuong,
                        chuan_hoa_dau_thanh=chuan_hoa_dau_thanh,
                        chuan_hoa_dau_cau= chuan_hoa_dau_cau,
                        split_word=split_word,
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
    # text = """
    # Hôm nay, Hà Nội ghi nhận 25 ca nhiễm mới covid19! Thành phố đang tăng cường các biện pháp phòng dịch. Người dân cần tuân thủ các quy định về giãn cách xã hội. Thủ tướng chính phủ đã chỉ đạo các bộ, ngành cần hành động nhanh chóng để ngăn chặn dịch bệnh lây lan, ông nói Chúng ta không được chủ quan!!
    # """
    text = f"Cộng hoàaa aa..."
    call_api(text)
    gui()
