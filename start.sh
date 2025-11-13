#!/bin/sh
set -e

echo "⏳ Syncing time..."

# Use ntpsec-ntpdate (new name)
if command -v ntpdate >/dev/null 2>&1; then
    ntpdate -u pool.ntp.org || true
elif command -v ntpsec-ntpdate >/dev/null 2>&1; then
    ntpsec-ntpdate -u pool.ntp.org || true
else
    echo "⚠ No ntpdate available (continuing anyway)"
fi

sleep 1

echo "🚀 Starting bot..."
python main.py
