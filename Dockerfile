FROM python:3.9-slim-buster
WORKDIR /flask
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]