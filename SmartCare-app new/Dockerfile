# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy entrypoint script and grant execute permissions
COPY smartcare-entrypoint.sh ./
RUN chmod +x smartcare-entrypoint.sh

# Copy all source code over
COPY . .

# Expose port 8000
EXPOSE 8000
