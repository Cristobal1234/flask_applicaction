FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV PYTHONHTTPSVERIFY=0

CMD ["python", "main.py"]
