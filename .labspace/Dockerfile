# Use a standard Python base image with development tools
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    openjdk-17-jdk \
    maven \
    && rm -rf /var/lib/apt/lists/*

# Set up Java environment
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Copy lab content
COPY labspace-exercises/ /app/labspace-exercises/
COPY labspace.yaml /app/
COPY README.md /app/

# Set working directory
WORKDIR /app

# Install Python dependencies for the lab
RUN pip install --no-cache-dir \
    pytest \
    psycopg2-binary \
    testcontainers[postgres]

# Expose port for lab interface
EXPOSE 8080

# Default command - start a shell for interactive lab
CMD ["/bin/bash"]
