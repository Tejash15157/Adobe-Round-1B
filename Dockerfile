FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY app /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "round1b.py"]
