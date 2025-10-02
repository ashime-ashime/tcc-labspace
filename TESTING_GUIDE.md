# Lab Testing Guide

This guide helps you test the Docker Testcontainers Lab before deploying it to TSEs.

## Prerequisites for Testing

Before testing the lab, ensure you have:

- [ ] Docker Desktop installed and running
- [ ] At least one programming language environment set up
- [ ] Internet connection for downloading container images
- [ ] Sufficient disk space (2-3 GB for container images)

## Testing Approach

### Phase 1: Environment Verification
### Phase 2: Language-Specific Testing
### Phase 3: Documentation Testing
### Phase 4: End-to-End Workflow Testing

---

## Phase 1: Environment Verification

### 1.1 Docker Environment Test

```bash
# Verify Docker is running
docker --version
docker info

# Test basic container functionality
docker run hello-world

# Pull required images for testing
docker pull postgres:15
docker pull postgres:13-alpine
```

### 1.2 Directory Structure Verification

```bash
# Verify lab structure
ls -la
tree . -L 3  # If tree is available, otherwise use ls -R
```

Expected structure:
```
├── README.md
├── DEPLOYMENT_GUIDE.md
├── docs/
├── exercises/
│   ├── java/
│   ├── go/
│   ├── nodejs/
│   └── python/
└── troubleshooting/
```

---

## Phase 2: Language-Specific Testing

Choose one or more languages to test based on your TSE team's preferences:

### 2.1 Java Testing (Recommended First)

#### Prerequisites
```bash
# Install Java 11+ and Maven
java --version
mvn --version
```

#### Test Steps
```bash
cd exercises/java

# 1. Verify project structure
ls -la src/

# 2. Compile the project
mvn clean compile

# 3. Run tests (this will download Testcontainers dependencies)
mvn test

# 4. Check test results
ls -la target/surefire-reports/
```

**Expected Results:**
- All tests should pass (12 test methods)
- PostgreSQL container should start and stop automatically
- Test reports should show successful execution

#### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| Maven not found | Install Maven: `brew install maven` (macOS) or download from Apache Maven |
| Java version < 11 | Update Java: `brew install openjdk@11` (macOS) |
| Docker connection error | Ensure Docker Desktop is running |
| Container pull timeout | Check internet connection, try pre-pulling: `docker pull postgres:15` |

### 2.2 Go Testing

#### Prerequisites
```bash
# Install Go 1.19+
go version
```

#### Test Steps
```bash
cd exercises/go

# 1. Initialize Go modules
go mod tidy

# 2. Download dependencies
go mod download

# 3. Run tests
go test -v

# 4. Check for race conditions
go test -race -v
```

**Expected Results:**
- All tests should pass
- No race conditions detected
- PostgreSQL container starts/stops cleanly

### 2.3 Node.js Testing

#### Prerequisites
```bash
# Install Node.js 18+
node --version
npm --version
```

#### Test Steps
```bash
cd exercises/nodejs

# 1. Install dependencies
npm install

# 2. Run TypeScript compilation
npm run build

# 3. Run tests
npm test

# 4. Check test coverage (optional)
npm run test:coverage
```

**Expected Results:**
- All tests pass
- TypeScript compiles without errors
- Container lifecycle managed properly

### 2.4 Python Testing

#### Prerequisites
```bash
# Install Python 3.8+
python --version
pip --version
```

#### Test Steps
```bash
cd exercises/python

# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run tests
pytest -v

# 4. Run with coverage
pytest --cov=. -v
```

**Expected Results:**
- All tests pass
- No import errors
- PostgreSQL container integration works

---

## Phase 3: Documentation Testing

### 3.1 README Validation

```bash
# Check main README
cat README.md | head -20

# Verify all links work (manual check)
# - Documentation links
# - Exercise links
# - External resource links
```

### 3.2 Exercise Documentation

```bash
# Check exercise documentation
ls exercises/*.md
head exercises/basic-database-testing.md
head exercises/testcontainers-cloud-setup.md
```

**Manual Checks:**
- [ ] Instructions are clear and step-by-step
- [ ] Code examples are properly formatted
- [ ] Prerequisites are clearly stated
- [ ] Learning objectives are realistic

### 3.3 Troubleshooting Documentation

```bash
# Check troubleshooting guides
head troubleshooting/README.md
head troubleshooting/COMMON_ISSUES.md
```

---

## Phase 4: End-to-End Workflow Testing

### 4.1 New User Simulation

Simulate a TSE going through the lab for the first time:

1. **Setup Phase:**
   ```bash
   # Follow setup instructions from docs/SETUP.md
   # Verify each prerequisite
   # Test basic Docker connectivity
   ```

2. **Exercise 1 - Basic Database Testing:**
   ```bash
   # Choose one language
   # Follow exercise instructions step by step
   # Run the provided code examples
   # Verify all tests pass
   ```

3. **Troubleshooting Simulation:**
   ```bash
   # Intentionally break something (e.g., stop Docker)
   # Use troubleshooting guide to fix it
   # Verify solutions work
   ```

### 4.2 Performance Testing

Test lab performance on different systems:

```bash
# Measure container startup time
time docker run --rm postgres:15 echo "Container started"

# Measure test execution time
time mvn test  # or equivalent for other languages

# Check resource usage
docker stats  # Run during tests
```

**Performance Benchmarks:**
- Container startup: < 30 seconds
- Test execution: < 2 minutes per language
- Memory usage: < 1GB during tests

---

## Testing Checklist

### Environment Setup
- [ ] Docker Desktop running
- [ ] Required language environments installed
- [ ] Internet connectivity verified
- [ ] Sufficient disk space available

### Java Implementation
- [ ] Project compiles successfully
- [ ] All 12 tests pass
- [ ] No compilation warnings
- [ ] Container lifecycle works properly

### Go Implementation (if testing)
- [ ] Go modules resolve correctly
- [ ] All tests pass
- [ ] No race conditions
- [ ] Clean container shutdown

### Node.js Implementation (if testing)
- [ ] Dependencies install successfully
- [ ] TypeScript compiles without errors
- [ ] All tests pass
- [ ] Async operations work correctly

### Python Implementation (if testing)
- [ ] Virtual environment creates successfully
- [ ] All dependencies install
- [ ] All tests pass
- [ ] No import errors

### Documentation
- [ ] README is clear and comprehensive
- [ ] Exercise instructions are step-by-step
- [ ] Troubleshooting guides are helpful
- [ ] All links work correctly

### End-to-End Workflow
- [ ] New user can follow setup guide
- [ ] Exercise 1 completes successfully
- [ ] Troubleshooting scenarios work
- [ ] Performance is acceptable

---

## Quick Test Script

Here's a quick test script you can run:

```bash
#!/bin/bash
# quick-test.sh - Quick lab validation

echo "=== Docker Testcontainers Lab Quick Test ==="

# Test 1: Docker availability
echo "Testing Docker..."
if docker --version > /dev/null 2>&1; then
    echo "✅ Docker is available"
else
    echo "❌ Docker is not available"
    exit 1
fi

# Test 2: Container functionality
echo "Testing container functionality..."
if docker run --rm hello-world > /dev/null 2>&1; then
    echo "✅ Docker containers work"
else
    echo "❌ Docker container test failed"
    exit 1
fi

# Test 3: PostgreSQL image
echo "Testing PostgreSQL image..."
if docker pull postgres:15 > /dev/null 2>&1; then
    echo "✅ PostgreSQL image available"
else
    echo "❌ Cannot pull PostgreSQL image"
    exit 1
fi

# Test 4: Directory structure
echo "Testing directory structure..."
if [[ -f "README.md" && -d "exercises" && -d "troubleshooting" ]]; then
    echo "✅ Lab structure is correct"
else
    echo "❌ Lab structure is incomplete"
    exit 1
fi

echo "=== Quick test completed successfully! ==="
```

---

## Troubleshooting Test Issues

### Common Test Failures

1. **Docker Connection Issues:**
   ```bash
   # Restart Docker Desktop
   # Check Docker daemon status
   docker info
   ```

2. **Container Image Issues:**
   ```bash
   # Clear Docker cache
   docker system prune -a
   
   # Re-pull images
   docker pull postgres:15
   ```

3. **Dependency Issues:**
   ```bash
   # For Java
   mvn clean
   rm -rf ~/.m2/repository/org/testcontainers
   
   # For Node.js
   rm -rf node_modules package-lock.json
   npm install
   
   # For Python
   rm -rf venv
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Permission Issues (Linux/macOS):**
   ```bash
   sudo usermod -aG docker $USER
   # Log out and back in
   ```

---

## Next Steps After Testing

Once testing is complete:

1. **Document Results:**
   - Note any issues found
   - Record performance benchmarks
   - Update documentation if needed

2. **Fix Issues:**
   - Address any failing tests
   - Update dependencies if needed
   - Improve documentation clarity

3. **Prepare for Deployment:**
   - Follow the DEPLOYMENT_GUIDE.md
   - Set up GitHub repository
   - Configure CI/CD if desired

4. **Train Instructors:**
   - Share testing results
   - Provide troubleshooting tips
   - Create instructor notes

---

## Getting Help

If you encounter issues during testing:

1. Check the troubleshooting guides in the `troubleshooting/` directory
2. Review Docker Desktop logs
3. Check container logs: `docker logs <container_id>`
4. Verify system requirements are met
5. Try testing on a clean environment

Remember: The goal is to ensure TSEs have a smooth experience, so thorough testing now will save time later!
