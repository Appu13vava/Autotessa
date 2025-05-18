FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt update && apt install -y git gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY . .

# Expose port for Flask health check
EXPOSE 8080

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "bot.py"]
