FROM python:3.9
COPY . .
RUN pip install -r requirement.txt
