FROM python:3.8.3

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY check_connection.py .
COPY .env .

CMD python check_connection.py
