from transformers import BertTokenizer
from gensim.utils import simple_preprocess

def word_BertTokenizer(text):
    tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
    text = tokenizer.tokenize(text)
    return text


def simple(text):
    text = simple_preprocess(text)
    return text

text = "Đây là một ví dụ để tách từ."
words = simple(text)
print(words)


# text = "Đây là một ví dụ để tách từ."
# tokens = word_BertTokenizer(text)
# print(tokens)