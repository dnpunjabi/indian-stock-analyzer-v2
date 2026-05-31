# Build/Runtime environment using Python 3.11-slim for standard efficiency
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable bufferless stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Set dynamic working directory
WORKDIR /app

# Install system dependencies (e.g. GCC/compilers if packages require compiling)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements first to leverage Docker layer caching
COPY backend/requirements.txt /app/backend/requirements.txt

# Install python dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Copy all application source code
COPY backend/ /app/backend/
COPY .env.example /app/.env.example

# Create the data directory for the SQLite database and set correct permissions
RUN mkdir -p /app/backend/data && chmod 777 /app/backend/data

# Create a non-privileged user and group for runtime execution
RUN groupadd -g 1000 appuser && \
    useradd -r -u 1000 -g appuser appuser && \
    chown -R appuser:appuser /app

# Switch to non-privileged runtime user
USER appuser

# Expose production port
EXPOSE 8000

# Run FastAPI production server using Uvicorn
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port ${PORT}"]
