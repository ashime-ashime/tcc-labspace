FROM docker/labspace:latest

# Copy lab content
COPY labspace-exercises/ /app/labspace-exercises/
COPY labspace.yaml /app/
COPY README.md /app/

# Set working directory
WORKDIR /app

# Expose port (LabSpace default)
EXPOSE 8080

# LabSpace will handle the rest
