#!/bin/sh
set -e

echo "⏳ Syncing system time..."

# Install ntpdate only if available (Debian base image)
if command -v ntpdate >/dev/null 2>&1; then
    ntpdate -u pool.ntp.org || ntpdate -u time.google.com || true
else
    echo "⚠️ ntpdate not found (will continue without manual sync)"
fi

sleep 1

echo "🚀 Starting TeraBox Downloader Bot..."
python main.py
