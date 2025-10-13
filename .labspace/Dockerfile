# Pre-Configured TCC LabSpace Dockerfile
FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    git \
    vim \
    nano \
    wget \
    unzip \
    gnupg \
    software-properties-common \
    ca-certificates \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic links for python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Docker (for Testcontainers Desktop simulation)
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update \
    && apt-get install -y docker-ce-cli \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages for TCC exercises
RUN pip3 install --no-cache-dir \
    testcontainers[postgres] \
    psycopg2-binary \
    pytest \
    requests

# Copy lab content
COPY . /workspace/
WORKDIR /workspace

# Create pre-configured TCC environment simulation
RUN mkdir -p /workspace/.testcontainers \
    && mkdir -p /workspace/.testcontainers-desktop

# Create simulated Testcontainers Desktop configuration
RUN cat > /workspace/.testcontainers-desktop/config.json << 'EOF'
{
  "version": "1.0.0",
  "settings": {
    "runtime": "cloud",
    "cloud": {
      "enabled": true,
      "organization": "tcc-lab-org-12345",
      "token": "tcct_lab_demo_token_abc123def456ghi789jkl012mno345pqr678stu901vwx234yz",
      "region": "us-east-1"
    },
    "docker": {
      "host": "unix:///var/run/docker.sock",
      "tls_verify": false
    },
    "logging": {
      "level": "info"
    }
  },
  "last_updated": "2025-01-10T10:30:00Z",
  "status": "configured_for_tcc"
}
EOF

# Create simulated TCC account status
RUN cat > /workspace/.testcontainers/tcc-account.json << 'EOF'
{
  "account_info": {
    "username": "tcc-lab-user",
    "email": "tcc-lab@example.com",
    "account_type": "free_trial",
    "tcc_org_id": "tcc-lab-org-12345",
    "tcc_plan_type": "free_trial"
  },
  "billing_details": {
    "plan": "free_trial",
    "quota_limit": 50,
    "quota_used": 15,
    "quota_remaining": 35,
    "quota_type": "one_time_only"
  },
  "service_accounts": [
    {
      "name": "lab-demo",
      "token": "tcct_lab_demo_token_abc123def456ghi789jkl012mno345pqr678stu901vwx234yz",
      "status": "active",
      "usage": "15 minutes"
    }
  ],
  "notes": "Pre-configured TCC account for lab exercises"
}
EOF

# Create interactive lab menu script
RUN cat > /workspace/start-lab.sh << 'EOF'
#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Clear screen and show welcome
clear
echo -e "${CYAN}🚀 Testcontainers Cloud (TCC) Lab for TSEs${NC}"
echo -e "${CYAN}==========================================${NC}"
echo ""
echo -e "${GREEN}✅ Pre-configured Environment Ready!${NC}"
echo -e "${GREEN}✅ TCC account: tcc-lab-org-12345${NC}"
echo -e "${GREEN}✅ Service account token: Configured${NC}"
echo -e "${GREEN}✅ Testcontainers Desktop: Simulated${NC}"
echo ""
echo -e "${YELLOW}📚 Available Break-and-Fix Exercises:${NC}"
echo ""
echo -e "${PURPLE}1. The Quota Mystery${NC}"
echo -e "   🎯 TCC Billing & Quota Investigation"
echo -e "   📁 Location: labspace-exercises/quota-mystery/"
echo ""
echo -e "${PURPLE}2. The Connection Mystery${NC}"
echo -e "   🎯 TCC Desktop Configuration Issues"
echo -e "   📁 Location: labspace-exercises/tcc-troubleshooting/"
echo ""
echo -e "${PURPLE}3. The CI/CD Mystery${NC}"
echo -e "   🎯 TCC GitHub Actions Integration"
echo -e "   📁 Location: labspace-exercises/ci-cd-mystery/"
echo ""
echo -e "${YELLOW}🔧 Quick Start Commands:${NC}"
echo -e "${BLUE}• Start Exercise 1:${NC} cd labspace-exercises/quota-mystery && cat README.md"
echo -e "${BLUE}• Start Exercise 2:${NC} cd labspace-exercises/tcc-troubleshooting && cat README.md"
echo -e "${BLUE}• Start Exercise 3:${NC} cd labspace-exercises/ci-cd-mystery && cat README.md"
echo ""
echo -e "${YELLOW}💡 Investigation Tips:${NC}"
echo -e "• Use 'cat' to view customer reports and logs"
echo -e "• Use 'cd' to navigate to exercise directories"
echo -e "• Use 'ls -la' to see all investigation materials"
echo -e "• Use 'grep' to search for specific information"
echo ""
echo -e "${CYAN}==========================================${NC}"
echo -e "${GREEN}Ready to investigate! Choose your exercise and start troubleshooting!${NC}"
echo -e "${CYAN}==========================================${NC}"
echo ""
EOF

# Make scripts executable
RUN chmod +x /workspace/start-lab.sh

# Create exercise navigation shortcuts
RUN cat > /workspace/exercise1.sh << 'EOF'
#!/bin/bash
cd /workspace/labspace-exercises/quota-mystery
echo "🔍 Starting Exercise 1: The Quota Mystery"
echo "📁 Current directory: $(pwd)"
echo "📋 Available files:"
ls -la
echo ""
echo "🚀 To start investigating, run: cat README.md"
EOF

RUN cat > /workspace/exercise2.sh << 'EOF'
#!/bin/bash
cd /workspace/labspace-exercises/tcc-troubleshooting
echo "🔍 Starting Exercise 2: The Connection Mystery"
echo "📁 Current directory: $(pwd)"
echo "📋 Available files:"
ls -la
echo ""
echo "🚀 To start investigating, run: cat README.md"
EOF

RUN cat > /workspace/exercise3.sh << 'EOF'
#!/bin/bash
cd /workspace/labspace-exercises/ci-cd-mystery
echo "🔍 Starting Exercise 3: The CI/CD Mystery"
echo "📁 Current directory: $(pwd)"
echo "📋 Available files:"
ls -la
echo ""
echo "🚀 To start investigating, run: cat README.md"
EOF

RUN chmod +x /workspace/exercise1.sh /workspace/exercise2.sh /workspace/exercise3.sh

# Run the interactive lab menu
CMD ["/bin/bash", "-c", "/workspace/start-lab.sh && /bin/bash"]