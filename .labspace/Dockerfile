# Interactive LabSpace with guided experience
FROM ubuntu:22.04

# Install basic tools for interactive experience
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    vim \
    nano \
    tree \
    less \
    && rm -rf /var/lib/apt/lists/*

# Copy lab content
COPY labspace-exercises/ /app/labspace-exercises/
COPY labspace.yaml /app/
COPY README.md /app/

# Create interactive lab starter script
RUN echo '#!/bin/bash\n\
echo "🎉 Welcome to Testcontainers Cloud Lab for TSEs!"\n\
echo "================================================="\n\
echo ""\n\
echo "📚 Available Exercises:"\n\
echo "  1. TCC Basics (45 min)"\n\
echo "  2. TCC Optimization (30 min)"\n\
echo "  3. TCC Troubleshooting (45 min)"\n\
echo ""\n\
echo "🚀 Quick Start:"\n\
echo "  cd labspace-exercises/tcc-basics\n\
echo "  cat README.md\n\
echo ""\n\
echo "💡 Tips:"\n\
echo "  - Use 'tree' to explore the lab structure\n\
echo "  - Use 'less README.md' to read exercise guides\n\
echo "  - All exercises are in /app/labspace-exercises/\n\
echo ""\n\
echo "🎯 Ready to start? Choose your exercise:"\n\
echo "  cd labspace-exercises/tcc-basics    # Start with Exercise 1"\n\
echo "  cd labspace-exercises/tcc-optimization  # Skip to Exercise 2"\n\
echo "  cd labspace-exercises/tcc-troubleshooting # Skip to Exercise 3"\n\
echo ""\n\
echo "Happy learning! 🚀"\n\
echo ""\n\
exec bash' > /app/start-lab.sh && chmod +x /app/start-lab.sh

# Set working directory
WORKDIR /app

# Expose port for lab interface
EXPOSE 8080

# Default command - start interactive lab experience
CMD ["/app/start-lab.sh"]
