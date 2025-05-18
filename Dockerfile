FROM python:3.10-slim

WORKDIR /app

# Install Git and pip
RUN apt update && apt install -y git && \
    pip install --upgrade pip

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your bot code
COPY . .

# Make start.sh executable
RUN chmod +x start.sh

# Start the bot
CMD ["bash", "start.sh"]
