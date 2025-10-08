# Minimal working LabSpace - just copy files and start
FROM ubuntu:22.04

# Copy lab content
COPY labspace-exercises/ /app/labspace-exercises/
COPY labspace.yaml /app/
COPY README.md /app/

# Set working directory
WORKDIR /app

# Expose port for lab interface
EXPOSE 8080

# Default command - start a shell for interactive lab
CMD ["/bin/bash"]
