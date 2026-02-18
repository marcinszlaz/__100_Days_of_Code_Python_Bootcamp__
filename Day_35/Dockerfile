FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt 
COPY weather_tracker.py .
CMD ["python", "-u", "weather_tracker.py"]
