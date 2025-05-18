#!/bin/bash

REPO_URL="https://github.com/AM-ROBOTS/AutoAnura"
APP_DIR="/AutoAnura"
LOG_FILE="/app_bot.log"

# Load .env if it exists
if [ -f "$APP_DIR/.env" ]; then
  echo "$(date) - Loading environment variables from .env" | tee -a $LOG_FILE
  export $(cat "$APP_DIR/.env" | xargs)
fi

# Clone the repository
if [ -z "$UPSTREAM_REPO" ]; then
  echo "$(date) - Cloning default repository..." | tee -a $LOG_FILE
  git clone "$REPO_URL" "$APP_DIR"
else
  echo "$(date) - Cloning custom repository from $UPSTREAM_REPO..." | tee -a $LOG_FILE
  git clone "$UPSTREAM_REPO" "$APP_DIR"
fi

cd "$APP_DIR" || { echo "Failed to enter $APP_DIR"; exit 1; }

# Install dependencies
echo "$(date) - Installing dependencies..." | tee -a $LOG_FILE
pip3 install --no-cache-dir -U -r requirements.txt >> $LOG_FILE 2>&1

# Run bot with restart loop
while true; do
  echo "$(date) - Starting bot..." | tee -a $LOG_FILE
  python3 bot.py >> $LOG_FILE 2>&1

  echo "$(date) - Bot crashed or stopped. Restarting in 5 seconds..." | tee -a $LOG_FILE
  sleep 5
done
