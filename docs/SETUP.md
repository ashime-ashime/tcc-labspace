# Lab Setup Instructions

This guide will help you set up your environment for the Docker Testcontainers lab.

## Prerequisites Check

Before starting, ensure you have the following installed:

### 1. Docker Desktop
- **Download**: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **Version**: Latest stable release
- **Verification**: Run `docker --version` and `docker-compose --version`

```bash
# Verify Docker is running
docker ps
```

### 2. Testcontainers Desktop
- **Download**: [Testcontainers Desktop](https://testcontainers.com/desktop/)
- **Installation**: Follow the platform-specific installation guide
- **Verification**: Launch the application and verify it can connect to Docker

### 3. Programming Language Setup

Choose your preferred language and set up the development environment:

#### Java Setup
```bash
# Install Java 11 or higher
java --version

# Install Maven or Gradle
mvn --version
# OR
gradle --version
```

#### Go Setup
```bash
# Install Go 1.19 or higher
go version

# Set up Go modules
go mod init testcontainers-lab
```

#### Node.js Setup
```bash
# Install Node.js 18 or higher
node --version
npm --version

# Install TypeScript (optional but recommended)
npm install -g typescript
```

#### Python Setup
```bash
# Install Python 3.8 or higher
python --version

# Install pip
pip --version

# Install virtual environment tools
pip install virtualenv
```

### 4. Git Setup
```bash
# Verify Git installation
git --version

# Configure Git (if not already done)
git config --global user.name "Your Name"
git config --global user.email "your.email@company.com"
```

## Lab Environment Setup

### 1. Clone the Lab Repository
```bash
# Clone the lab repository
git clone <repository-url>
cd docker-testcontainers-lab

# Verify the lab structure
ls -la
```

### 2. Choose Your Language Track
Navigate to your preferred language directory:
```bash
# For Java
cd exercises/java

# For Go
cd exercises/go

# For Node.js
cd exercises/nodejs

# For Python
cd exercises/python
```

### 3. Install Dependencies

#### Java (Maven)
```bash
cd exercises/java
mvn clean install
```

#### Java (Gradle)
```bash
cd exercises/java
./gradlew build
```

#### Go
```bash
cd exercises/go
go mod tidy
```

#### Node.js
```bash
cd exercises/nodejs
npm install
```

#### Python
```bash
cd exercises/python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Verify Testcontainers Setup

#### Test Docker Connectivity
```bash
# Verify Docker is accessible
docker run hello-world
```

#### Test Testcontainers Desktop
1. Launch Testcontainers Desktop application
2. Verify it shows "Connected" status
3. Check that Docker daemon is accessible

#### Run a Simple Test
Execute the basic verification test for your chosen language:

```bash
# Java
mvn test -Dtest=BasicTest

# Go
go test -v ./basic_test.go

# Node.js
npm test -- --testNamePattern="Basic Test"

# Python
pytest basic_test.py -v
```

## Testcontainers Cloud Setup (Optional)

For advanced exercises, you may want to set up Testcontainers Cloud:

### 1. Create Testcontainers Cloud Account
- Visit [Testcontainers Cloud](https://testcontainers.com/cloud/)
- Sign up for a free trial account
- Note your API token

### 2. Configure Cloud Access
```bash
# Set environment variable (replace with your token)
export TC_CLOUD_TOKEN=your_token_here

# Or create a .env file
echo "TC_CLOUD_TOKEN=your_token_here" > .env
```

### 3. Enable Cloud Mode in Testcontainers Desktop
1. Open Testcontainers Desktop
2. Go to Settings
3. Enable "Use Testcontainers Cloud"
4. Enter your API token
5. Save settings

## Troubleshooting Setup Issues

### Docker Issues
```bash
# Check Docker daemon status
docker info

# Restart Docker Desktop if needed
# On macOS: Docker Desktop -> Restart
# On Windows: Docker Desktop -> Restart
# On Linux: sudo systemctl restart docker
```

### Port Conflicts
If you encounter port conflicts:
```bash
# Check what's using a port
lsof -i :5432  # For PostgreSQL
lsof -i :3306  # For MySQL
lsof -i :6379  # For Redis

# Kill processes if necessary
kill -9 <PID>
```

### Permission Issues (Linux/macOS)
```bash
# Add user to docker group
sudo usermod -aG docker $USER
# Log out and back in for changes to take effect
```

## Verification Checklist

Before starting the lab exercises, verify:

- [ ] Docker Desktop is running
- [ ] Testcontainers Desktop is installed and connected
- [ ] Your chosen programming language is set up
- [ ] Dependencies are installed successfully
- [ ] Basic test runs without errors
- [ ] Git is configured
- [ ] Lab repository is cloned locally

## Getting Help

If you encounter issues during setup:

1. **Check the Troubleshooting Guide**: `troubleshooting/README.md`
2. **Review Common Issues**: `troubleshooting/COMMON_ISSUES.md`
3. **Contact Lab Instructors**: Use the provided support channels
4. **Testcontainers Community**: [Slack](https://slack.testcontainers.org/) or [GitHub Discussions](https://github.com/testcontainers/testcontainers-java/discussions)

## Next Steps

Once setup is complete:
1. Read the [Lab Overview](LAB_OVERVIEW.md)
2. Start with [Exercise 1: Basic Database Testing](../exercises/basic-database-testing.md)
3. Follow the exercises in order for your chosen language
