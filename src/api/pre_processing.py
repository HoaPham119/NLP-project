import re
from bs4 import BeautifulSoup
from pyvi import ViTokenizer
import unicodedata
from underthesea import word_tokenize
# import chardet
from underthesea import sent_tokenize
from underthesea import text_normalize

# Hàm loại bỏ mã HTML
def remove_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# Hàm loại bỏ ký tự đặc biệt
def remove_special_characters(text):
    # Loại bỏ tất cả các ký tự không phải là chữ cái hoặc số
    return re.sub(r'[^a-zA-Z0-9\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ.!?]', ' ', text)

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

# Danh sách các từ dừng tiếng Việt
stop_words = set([
    "và", "là", "của", "có", "với", "cho", "một", "các", "được", "trên", "lại", "thì", "làm", "ra", "đi", "còn", "này", "ở", "đây", "này", "ấy", "vậy", "thế", "như", "nhiều", "những", "cả", "đã", "rồi", "sẽ", "khi", "đang", "vẫn", "nên", "theo", "vào", "hơn", "về"
])

# Chuẩn hoá dấu thanh:
def text_normalize_f(text):
    text = text_normalize(text)
    return text

# Bước 4: Tách từ
def word_tokenize(text):
    return ViTokenizer.tokenize(text)

# Tách câu:
def sentence_tokenize(text):
    text = sent_tokenize(text)
    text_new_sent = []
    for _text in text:
        text_new = re.sub(r'[^a-zA-Z0-9\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ_]', '', _text)
        if len(text_new) == 0:
            continue
        # print(text_new)
        text_new_sent.append(text_new)
        
    return text_new_sent


def chuan_hoa_unicode(text):
    text = unicodedata.normalize('NFC', text)
    return text

# Hàm loại bỏ từ dừng
def remove_stop_words(text):
    words = ViTokenizer.tokenize(text)
    words = text.split()
    # words = word_tokenize(text)
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


def split_sentences(text):
    # Sử dụng regex để tách câu
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    return sentences

def get_final_text(text):
    for _text in text:
        if "final_text" in locals():
            final_text = final_text + " " + _text
        else:
            final_text = _text
    return final_text

# Hàm tổng hợp để tiền xử lý văn bản
def preprocess_text(text, 
                    clean = True,
                    standardized = True,
                    split_word = True,
                    split_sent = True
                    ):
    if clean:
        # Loại bỏ mã html
        text = remove_html(text)
        # Loại bỏ kí tự đặc biệt
        text = remove_special_characters(text)
        # Loại khoảng trắng thừa
        text = remove_extra_whitespace(text)

    # Chuẩn hoá dữ liệu
    if standardized:
        # Chuẩn hoá unicode dựng sẵng:
        text = chuan_hoa_unicode(text)
        text = to_lowercase(text)
        # Chuẩn hoá dấu thanh
        text = text_normalize_f(text)
        # Loại khoảng trắng thừa
        text = remove_extra_whitespace(text)
    if split_word:
        # Tách từ
        # Tách từ
        text = word_tokenize(text)
        # Chuẩn hoá dấu câu
        text = normalize_punctuation(text)
        # Loại khoảng trắng thừa
        text = remove_extra_whitespace(text)
    # Tách câu
    if split_sent:
        text = sentence_tokenize(text)
    elif clean:
        # Loại bỏ kí tự đặc biệt
        # text = remove_special_characters(text)
        text = re.sub(r'[^a-zA-Z0-9\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ_]', ' ', text)
        # Loại khoảng trắng thừa
        text = remove_extra_whitespace(text)
    
    # Get final text
    # text = get_final_text(text)

    return text

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
processed_text = preprocess_text(text)
print("Văn bản sau khi tiền xử lý:", processed_text)
print()

