# Default to Python 3.12
ARG BASE_IMAGE=python:3.12-slim
FROM ${BASE_IMAGE}

# Set the working directory for your application
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y dos2unix && rm -rf /var/lib/apt/lists/*

# Copy dependency files first for better caching
COPY pyproject.toml /app/
# Copy poetry.lock if it exists
COPY poetry.loc[k] /app/

# Install Python dependencies
RUN pip install --no-cache-dir -U pip==25.2 setuptools==80.9.0 && \
    pip install --no-cache-dir poetry==1.8.3 && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Copy entrypoint script
COPY entrypoint.sh /app/

# Copy application code
COPY *.py /app/


# Fix line endings and permissions
RUN dos2unix /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

# Set the entrypoint for the container
ENTRYPOINT ["/app/entrypoint.sh"]