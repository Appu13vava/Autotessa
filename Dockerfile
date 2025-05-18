FROM python:3.10-slim

WORKDIR /app

# Install Git and upgrade pip
RUN apt update && apt install -y git && \
    pip install --upgrade pip

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your bot code
COPY . .

# Run the bot directly
CMD ["python", "bot.py"]
