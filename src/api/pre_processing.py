import re

import unicodedata

import sys
import os
from underthesea import sent_tokenize
from underthesea import text_normalize
from bs4 import BeautifulSoup
from pyvi import ViTokenizer
from underthesea import word_tokenize

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
with open('data/vietnamese-stopwords.txt', 'r', encoding='utf-8') as file:
    stop_words = [line.strip() for line in file]

# Hàm loại bỏ mã HTML
def remove_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# Hàm loại bỏ ký tự đặc biệt

def remove_special_characters(text):
    # Loại bỏ tất cả các ký tự không phải là chữ cái hoặc số
    return re.sub(r'[^a-zA-Z0-9\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ.!?]', ' ', text)

# Hàm chuyển đổi chữ hoa thành chữ thường
def to_lowercase(text):
    return text.lower()

# Hàm loại bỏ khoảng trắng thừa
def remove_extra_whitespace(text):
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace(" .", ".")
    text = text.replace(" !", "!")
    text = text.replace(" ?", "?")
    text = text.replace(" ,", ",")
    return text

# Chuẩn hoá dấu thanh:
def text_normalize_f(text):
    text = text_normalize(text)
    text = remove_extra_whitespace(text)
    return text

# Bước 4: Tách từ
def word_tokenize(text):
    return ViTokenizer.tokenize(text)

# Tách câu:
def sentence_tokenize(text):
    text = sent_tokenize(text)
    text_new_sent = []
    for _text in text:
        text_new = re.sub(
            r'[^a-zA-Z0-9\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ_]', ' ', _text)
        text_new = re.sub(r'\s+', ' ', text_new).strip()
        
        if len(text_new) == 0:
            continue
        if text_new[-1] == " ":
            text_new = text_new[:-1]
        # print(text_new)
        text_new_sent.append(text_new)

    return text_new_sent

# Chuẩn hoá unicode
def chuan_hoa_unicode(text):
    text = unicodedata.normalize('NFC', text)
    return text

# Hàm loại bỏ từ dừng
def remove_stop_words(text):
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)
    # return filtered_words


def normalize_punctuation(text):
    # Loại bỏ khoảng trắng thừa trước dấu câu
    text = re.sub(r'\s+([,.!?])', r'\1', text)
    # Thêm khoảng trắng sau dấu câu nếu chưa có
    text = re.sub(r'([,.!?])([^\s])', r'\1 \2', text)
    # Loại bỏ khoảng trắng thừa
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# def get_final_text(text):
#     for _text in text:
#         if "final_text" in locals():
#             final_text = final_text + " " + _text
#         else:
#             final_text = _text
#     return final_text

# Hàm tổng hợp để tiền xử lý văn bản
def preprocess_text(text,
                    clean_html=True,
                    clean_special_char=True,
                    clean_extra_whitespace=True,
                    chuan_hoa_unicode_action=True,
                    chuan_hoa_chu_thuong= True,
                    chuan_hoa_dau_thanh=True,
                    split_word=True,
                    split_sent=True,
                    remove_sw=True
                    ):
    if clean_html:
        text = remove_html(text)
    if clean_special_char:
        text = remove_special_characters(text)
    if clean_extra_whitespace:
        # Loại khoảng trắng thừa
        text = remove_extra_whitespace(text)
    # Chuẩn hoá dữ liệu
    if chuan_hoa_unicode_action:
        text = chuan_hoa_unicode(text)
    if chuan_hoa_chu_thuong:
        text = to_lowercase(text)
    if chuan_hoa_dau_thanh:
        text = text_normalize_f(text)

    if split_word:
        # Tách từ
        # Tách từ
        text = word_tokenize(text)
        # Chuẩn hoá dấu câu
        text = normalize_punctuation(text)
        # Loại khoảng trắng thừa
        text = remove_extra_whitespace(text)
    
    if remove_sw:
        text = remove_stop_words(text=text)
    # Tách câu
    if split_sent:
        text = sentence_tokenize(text)
        return text
    elif clean_special_char:
        # Loại bỏ kí tự đặc biệt
        # text = remove_special_characters(text)
        text = re.sub(
            r'[^a-zA-Z0-9\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ_]', ' ', text)
        # Loại khoảng trắng thừa
        text = remove_extra_whitespace(text)

    # Get final text
    # text = get_final_text(text)

    return [text]

if __name__ == "__main__":
    # text = """<p>Hôm nay, Hà Nội ghi nhận 25 ca nhiễm mới covid-19!   Thành phố đang tăng cường các biện pháp phòng dịch   . Người dân cần tuân thủ các quy định về giãn cách xã hội . Thủ tướng chính phủ đã chỉ đạo các bộ, ngành cần hành động nhanh chóng   để ngăn chặn dịch bệnh lây lan, ông nói: "Chúng ta không được chủ quan"!!</p>
    # """
    text = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Tin Tức - VnExpress</title>
    </head>
    <body>
        <div class="article">
            <h1>Tin tức mới nhất</h1>
            <p>
                Chào mừng bạn đến với <strong>VnExpress</strong>, nơi cập nhật <a href="https://vnexpress.net">tin tức</a> nhanh chóng nhất!
                Hôm nay, chúng tôi có các tin đặc biệt sau:
            </p>
            <ul>
                <li>Sự kiện oà ạt diễn ra vào ngày hôm qua</li>
                <li>Các biện pháp phòng chống Covid-19 đang được thực hiện quyết liệt</li>
                <li>Giá vàng tăng mạnh, gây chú ý lớn cho thị trường!</li>
            </ul>
            <p>
                Đừng bỏ lỡ các bản tin đặc biệt khác: thể thao, kinh doanh, đời sống, và nhiều hơn nữa! 
                Đăng ký nhận bản tin ngay hôm nay để không bỏ lỡ thông tin <em>hot</em> nhất.
            </p>
            <footer>
                <p>&copy; 2024 VnExpress. All rights reserved. Liên hệ: info@vnexpress.net</p>
            </footer>
        </div>
    </body>
    </html>


    """
    # Tiền xử lý văn bản
    processed_text = preprocess_text(text, split_sent=False)
    print("Văn bản sau khi tiền xử lý:", processed_text)
    print()
