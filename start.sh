#!/bin/sh
set -e

# try to install ntpdate (works on debian-based images)
if command -v apt-get >/dev/null 2>&1; then
  apt-get update -y || true
  apt-get install -y ntpdate || true
fi

# Try syncing time with public NTP servers (best-effort; continue on failure)
ntpdate -u pool.ntp.org || ntpdate -u time.google.com || true

# small sleep to let system apply time
sleep 1

# Start the bot
python main.py
