# backend_server_2/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py

EXPOSE 5001
CMD ["python", "app.py"]
