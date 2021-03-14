FROM python:3.9-slim as builder
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

FROM builder
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY /web /app
RUN adduser --disabled-password --shell /bin/bash --gecos "User" apprunner && chown -R apprunner /app
USER apprunner
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "server:server"]