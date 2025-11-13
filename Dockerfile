FROM python:3.11-slim

WORKDIR /app

# Install ntpsec-ntpdate (replacement for ntpdate)
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ntpsec-ntpdate && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /app/start.sh

ENV PYTHONUNBUFFERED=1

CMD ["/bin/sh", "/app/start.sh"]
