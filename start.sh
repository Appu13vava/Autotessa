#!/bin/bash

REPO_URL="https://github.com/AM-ROBOTS/AutoAnura"
APP_DIR="/AutoAnura"
LOG_FILE="/app_bot.log"

# Clone repo if not exists or if UPSTREAM_REPO is set
if [ -z "$UPSTREAM_REPO" ]; then
  echo "$(date) - Cloning main repository..." | tee -a $LOG_FILE
  git clone $REPO_URL $APP_DIR
else
  echo "$(date) - Cloning custom repo from $UPSTREAM_REPO..." | tee -a $LOG_FILE
  git clone $UPSTREAM_REPO $APP_DIR
fi

cd $APP_DIR || exit 1

# Install dependencies
echo "$(date) - Installing dependencies..." | tee -a $LOG_FILE
pip3 install -U -r requirements.txt

# Run bot with restart loop
while true; do
  echo "$(date) - Starting bot..." | tee -a $LOG_FILE
  python3 bot.py >> $LOG_FILE 2>&1

  echo "$(date) - Bot crashed or stopped. Restarting in 5 seconds..." | tee -a $LOG_FILE
  sleep 5
done
