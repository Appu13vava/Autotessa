#!/bin/bash

# Clone repo
if [ -z "$UPSTREAM_REPO" ]
then
  echo "Cloning main Repository"
  git clone https://github.com/AM-ROBOTS/AutoAnura /AutoAnura
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO"
  git clone $UPSTREAM_REPO /AutoAnura
fi

cd /AutoAnura

# Install requirements
pip3 install -U -r requirements.txt

# Start a dummy HTTP server for Koyeb health check (on port 8080)
python3 -m http.server 8080 &

# Start your bot
echo "Starting Bot...."
python3 bot.py
