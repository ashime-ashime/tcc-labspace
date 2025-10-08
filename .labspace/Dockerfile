# Interactive LabSpace Dockerfile
FROM ubuntu:22.04

# Install basic tools and dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    git \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic links for python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Copy lab content
COPY . /workspace/
WORKDIR /workspace

# Create a welcome script
COPY <<EOF /workspace/welcome.sh
#!/bin/bash
clear
echo "🚀 Testcontainers Cloud (TCC) Lab for TSEs"
echo "=========================================="
echo ""
echo "📚 Available Exercises:"
echo "1. TCC Architecture and Advanced Configuration"
echo "2. Enterprise TCC CI/CD Integration"  
echo "3. Advanced TSE TCC Troubleshooting"
echo ""
echo "📁 Exercise Locations:"
echo "• Exercise 1: labspace-exercises/tcc-setup/"
echo "• Exercise 2: labspace-exercises/tcc-github-actions/"
echo "• Exercise 3: labspace-exercises/tcc-troubleshooting/"
echo ""
echo "🔧 Quick Start Commands:"
echo "• View Exercise 1: cat labspace-exercises/tcc-setup/README.md"
echo "• View Exercise 2: cat labspace-exercises/tcc-github-actions/README.md"
echo "• View Exercise 3: cat labspace-exercises/tcc-troubleshooting/README.md"
echo ""
echo "💡 Tip: Use 'cat' to view exercise files, 'cd' to navigate directories"
echo "=========================================="
echo ""
EOF

# Make welcome script executable
RUN chmod +x /workspace/welcome.sh

# Run welcome script and start bash
CMD ["/bin/bash", "-c", "/workspace/welcome.sh && /bin/bash"]