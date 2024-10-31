FROM mcr.microsoft.com/playwright/python:v1.42.0-jammy

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (already in the image, but ensures matching version)
RUN playwright install chromium

# Copy app code
COPY . .

