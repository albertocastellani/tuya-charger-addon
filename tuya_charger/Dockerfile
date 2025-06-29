FROM python:3.11-slim
WORKDIR /data
COPY run.py .
RUN pip install paho-mqtt requests
CMD ["python", "run.py", "--config", "/data/options.json"]
