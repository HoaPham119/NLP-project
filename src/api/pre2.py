import py_vncorenlp
import os
path = os.path.dirname(__file__)+"/../../models/VnCoreNLP"
# Automatically download VnCoreNLP components from the original repository
# and save them in some local working folder
py_vncorenlp.download_model(save_dir=path)

# Load VnCoreNLP from the local working folder that contains both `VnCoreNLP-1.2.jar` and `models` 
model = py_vncorenlp.VnCoreNLP(save_dir=path)
# Equivalent to: model = py_vncorenlp.VnCoreNLP(annotators=["wseg", "pos", "ner", "parse"], save_dir='/absolute/path/to/vncorenlp')

# Annotate a raw corpus
model.annotate_file(input_file="/absolute/path/to/input/file", output_file="/absolute/path/to/output/file")

# Annotate a raw text
model.print_out(model.annotate_text("Ông Nguyễn Khắc Chúc  đang làm việc tại Đại học Quốc gia Hà Nội. Bà Lan, vợ ông Chúc, cũng làm việc tại đây."))