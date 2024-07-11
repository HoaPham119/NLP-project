import requests
import json
import streamlit as st

base_url = "http://0.0.0.0:8000/"
path_url = "api/v1/pre-processing"
headers = {"Content-Type": "application/json"}

def call_api(text,
             clean=True,
             standardized=True,
             split_word=True,
             split_sent=True,
             remove_sw=True
             ):
    param = {
        "text": text,
        "clean": clean,
        "standardized": standardized,
        "split_word": split_word,
        "split_sent": split_sent,
        "remove_sw": remove_sw,

    }
    url = base_url + path_url + "?" + f"text={text}&clean={clean}&standardized={standardized}&split_word={split_word}&split_sent={split_sent}&remove_sw={remove_sw}"
    rsp = requests.get(url=url, params=param, headers=headers)
    data = json.loads(rsp.text)["data"]
    return data
    

def gui():
    st.title("ĐỒ ÁN XỬ LÝ VĂN BẢN TIẾNG VIỆT")
    
    text = st.text_input("Nhập vào đoạn văn bản cần xử lý:")
    st.write("Lựa chọn các tác vụ bạn mong muốn:")
    clean = st.checkbox("Làm sạch văn bản")
    standardized = st.checkbox("Chuẩn hoá văn bản")
    split_word = st.checkbox("Tách từ")
    split_sent = st.checkbox("Tách câu")
    remove_sw = st.checkbox("Loại bỏ stopwords")
    # Nút Start
    if st.button('Xử lý'):
        data = call_api(text = text,
             clean=clean,
             standardized=standardized,
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
    text = """
    Hôm nay, Hà Nội ghi nhận 25 ca nhiễm mới covid19! Thành phố đang tăng cường các biện pháp phòng dịch. Người dân cần tuân thủ các quy định về giãn cách xã hội. Thủ tướng chính phủ đã chỉ đạo các bộ, ngành cần hành động nhanh chóng để ngăn chặn dịch bệnh lây lan, ông nói Chúng ta không được chủ quan!!
    """
    # call_api(text)
    gui()