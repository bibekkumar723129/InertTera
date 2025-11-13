FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install ntpdate for time synchronization
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ntpdate && \
    rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure start.sh is executable
RUN chmod +x /app/start.sh

# Prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Start with our script (sync time → launch bot)
CMD ["/bin/sh", "/app/start.sh"]
