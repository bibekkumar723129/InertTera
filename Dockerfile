FROM python:3.11-slim

WORKDIR /app
COPY . /app

# Install ntpdate (for time sync) and any other system deps
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ntpdate && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Add start script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

ENV PYTHONUNBUFFERED=1

CMD ["/bin/sh", "/app/start.sh"]
