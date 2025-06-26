FROM python:3.10-slim

RUN pip install flask prometheus_client requests

COPY bind_exporter.py /bind_exporter.py

CMD ["python", "/bind_exporter.py"]
