#!/bin/bash
# quick-test.sh - Quick lab validation script

set -e  # Exit on any error

echo "=== Docker Testcontainers Lab Quick Test ==="
echo

# Test 1: Docker availability
echo "🔍 Testing Docker availability..."
if docker --version > /dev/null 2>&1; then
    echo "✅ Docker is available: $(docker --version)"
else
    echo "❌ Docker is not available"
    echo "   Please install and start Docker Desktop"
    exit 1
fi

# Test 2: Docker daemon running
echo
echo "🔍 Testing Docker daemon..."
if docker info > /dev/null 2>&1; then
    echo "✅ Docker daemon is running"
else
    echo "❌ Docker daemon is not running"
    echo "   Please start Docker Desktop"
    exit 1
fi

# Test 3: Container functionality
echo
echo "🔍 Testing container functionality..."
if docker run --rm hello-world > /dev/null 2>&1; then
    echo "✅ Docker containers work correctly"
else
    echo "❌ Docker container test failed"
    echo "   Check Docker installation and permissions"
    exit 1
fi

# Test 4: PostgreSQL image
echo
echo "🔍 Testing PostgreSQL image availability..."
if docker pull postgres:15-alpine > /dev/null 2>&1; then
    echo "✅ PostgreSQL image downloaded successfully"
else
    echo "❌ Cannot pull PostgreSQL image"
    echo "   Check internet connection"
    exit 1
fi

# Test 5: Directory structure
echo
echo "🔍 Testing lab directory structure..."
missing_items=()

if [[ ! -f "README.md" ]]; then
    missing_items+=("README.md")
fi

if [[ ! -d "exercises" ]]; then
    missing_items+=("exercises/")
fi

if [[ ! -d "troubleshooting" ]]; then
    missing_items+=("troubleshooting/")
fi

if [[ ! -f "exercises/java/pom.xml" ]]; then
    missing_items+=("exercises/java/pom.xml")
fi

if [[ ! -f "exercises/go/go.mod" ]]; then
    missing_items+=("exercises/go/go.mod")
fi

if [[ ! -f "exercises/nodejs/package.json" ]]; then
    missing_items+=("exercises/nodejs/package.json")
fi

if [[ ! -f "exercises/python/requirements.txt" ]]; then
    missing_items+=("exercises/python/requirements.txt")
fi

if [[ ${#missing_items[@]} -eq 0 ]]; then
    echo "✅ Lab structure is complete"
else
    echo "❌ Missing items:"
    for item in "${missing_items[@]}"; do
        echo "   - $item"
    done
    exit 1
fi

# Test 6: SQL initialization script
echo
echo "🔍 Testing SQL initialization script..."
if [[ -f "exercises/java/src/test/resources/init.sql" ]]; then
    echo "✅ SQL initialization script found"
else
    echo "❌ SQL initialization script missing"
    exit 1
fi

# Test 7: Check for common tools (optional)
echo
echo "🔍 Checking for development tools (optional)..."

# Java
if command -v java > /dev/null 2>&1; then
    echo "✅ Java found: $(java -version 2>&1 | head -n 1)"
else
    echo "⚠️  Java not found (needed for Java exercises)"
fi

if command -v mvn > /dev/null 2>&1; then
    echo "✅ Maven found: $(mvn --version | head -n 1)"
else
    echo "⚠️  Maven not found (needed for Java exercises)"
fi

# Go
if command -v go > /dev/null 2>&1; then
    echo "✅ Go found: $(go version)"
else
    echo "⚠️  Go not found (needed for Go exercises)"
fi

# Node.js
if command -v node > /dev/null 2>&1; then
    echo "✅ Node.js found: $(node --version)"
else
    echo "⚠️  Node.js not found (needed for Node.js exercises)"
fi

if command -v npm > /dev/null 2>&1; then
    echo "✅ npm found: $(npm --version)"
else
    echo "⚠️  npm not found (needed for Node.js exercises)"
fi

# Python
if command -v python3 > /dev/null 2>&1; then
    echo "✅ Python found: $(python3 --version)"
else
    echo "⚠️  Python not found (needed for Python exercises)"
fi

if command -v pip3 > /dev/null 2>&1; then
    echo "✅ pip found: $(pip3 --version | head -n 1)"
else
    echo "⚠️  pip not found (needed for Python exercises)"
fi

echo
echo "=== Quick Test Summary ==="
echo "✅ Core requirements met - lab is ready for basic testing"
echo
echo "Next steps:"
echo "1. Choose a language to test (Java recommended first)"
echo "2. Follow the TESTING_GUIDE.md for detailed testing"
echo "3. Run actual tests in your chosen language directory"
echo
echo "Example for Java:"
echo "  cd exercises/java"
echo "  mvn test"
echo
echo "Example for Go:"
echo "  cd exercises/go"
echo "  go test -v"
echo
echo "Example for Node.js:"
echo "  cd exercises/nodejs"
echo "  npm install && npm test"
echo
echo "Example for Python:"
echo "  cd exercises/python"
echo "  python -m venv venv && source venv/bin/activate"
echo "  pip install -r requirements.txt && pytest -v"

echo
echo "=== Quick test completed successfully! ==="
