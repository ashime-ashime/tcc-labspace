# Use a base image that already has Java and Maven
FROM maven:3.9.11-eclipse-temurin-11

# Install Python and pip (keep it simple)
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Copy lab content
COPY labspace-exercises/ /app/labspace-exercises/
COPY labspace.yaml /app/
COPY README.md /app/

# Set working directory
WORKDIR /app

# Install Python dependencies for the lab
RUN pip3 install --no-cache-dir -r labspace-exercises/tcc-basics/python/requirements.txt

# Expose port for lab interface
EXPOSE 8080

# Default command - start a shell for interactive lab
CMD ["/bin/bash"]
