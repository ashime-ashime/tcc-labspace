# Exercise 1: TCC Architecture and Advanced Configuration

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Understand TCC architecture and infrastructure
- Configure advanced TCC settings for enterprise environments
- Diagnose TCC connectivity and performance issues
- Implement TCC optimization strategies

## 📚 Prerequisites

- Docker Desktop with advanced configuration knowledge
- Understanding of container orchestration and networking
- Experience with CI/CD pipelines and service accounts
- Familiarity with enterprise authentication systems

## 🏗️ TCC Architecture Deep Dive

### Infrastructure Components

TCC operates on a distributed architecture:
- **Edge Locations**: Regional TCC endpoints for low latency
- **Container Orchestration**: Kubernetes-based container management
- **Image Registry**: Cached container images for faster startup
- **Authentication Layer**: OAuth2/JWT-based service accounts

### Network Architecture

```
Local Machine → Testcontainers Desktop → TCC API Gateway → Regional Workers
                     ↓
                Local Docker Socket (bypass for cloud execution)
```

## 🚀 Step 1: Install and Configure Testcontainers Desktop

### 1.1 Download Testcontainers Desktop

**For Mac:**
```bash
# Install via Homebrew (recommended)
brew install atomicjar/tap/testcontainers-desktop

# Or download from: https://testcontainers.com/desktop/
```

**For Windows:**
1. Go to https://testcontainers.com/desktop/
2. Download the Windows installer
3. Run the installer as administrator

**For Linux:**
```bash
# Download the .deb package
wget https://github.com/atomicjar/testcontainers-desktop/releases/latest/download/testcontainers-desktop-linux-amd64.deb
sudo dpkg -i testcontainers-desktop-linux-amd64.deb
```

### 1.2 Start Testcontainers Desktop

```bash
# Start the application
testcontainers-desktop

# Verify it's running
ps aux | grep testcontainers-desktop
```

### 1.3 Sign Up for Testcontainers Cloud

1. **Open Testcontainers Desktop** (should open automatically after install)
2. **Click "Sign up for free"** button
3. **Create account** with your email
4. **Verify email** if required
5. **Sign in** to the Desktop app

### 1.4 Verify Connection

**Look for these indicators:**
- ✅ Desktop app shows "Connected to Testcontainers Cloud"
- ✅ Green status indicator in the app
- ✅ No error messages in the app

**If not connected:**
- Check internet connection
- Restart the Desktop app
- Sign out and sign back in

## 🧪 Step 2: Run Your First TCC Test

### 2.1 Navigate to the Test Directory

```bash
# You should be in the lab directory
pwd
# Expected: /workspace or similar

# Navigate to the Python test
cd labspace-exercises/tcc-setup/python
ls -la
# Expected: test_simple.py should be visible
```

### 2.2 Install Python Dependencies

```bash
# Install required packages
pip3 install testcontainers[postgres] psycopg2-binary pytest

# Verify installation
python3 -c "import testcontainers; print('✅ Testcontainers installed')"
```

### 2.3 Run the Test

```bash
# Run the simple PostgreSQL test
python3 -m pytest test_simple.py -v

# Alternative: Run directly
python3 test_simple.py
```

### 2.4 Expected Output

**If TCC is working correctly, you should see:**
```
✅ PostgreSQL test completed successfully in TCC!
```

**If running in cloud, you'll also see:**
- Testcontainers Desktop shows "Cloud" activity
- No local Docker containers created
- Test completes faster after first run

### 2.5 Troubleshooting

**If you get errors:**

1. **Import Error:**
   ```bash
   # Solution: Install missing package
   pip3 install testcontainers
   ```

2. **Connection Error:**
   ```bash
   # Check if TCC is connected
   # Open Testcontainers Desktop app
   # Verify green "Connected" status
   ```

3. **Permission Error:**
   ```bash
   # Solution: Use python3 instead of python
   python3 test_simple.py
   ```

## 📊 Step 3: Monitor TCC Usage

### 3.1 Check Usage in Desktop App

1. Open Testcontainers Desktop
2. Look for usage statistics
3. Note your remaining cloud minutes
4. Check the activity log

### 3.2 Understand Free Tier Limits

**Free Tier Includes:**
- 50 minutes of cloud runtime per month
- Unlimited local usage (with Desktop app)
- No system privileges required
- Works with public and private registries

## 🎯 Step 4: Compare Local vs Cloud

### 4.1 Run Test Locally (for comparison)

```bash
# Temporarily disconnect from TCC in Desktop app
# Run the same test
pytest test_simple.py -v
```

**Notice the differences:**
- Local Docker containers created
- Uses your laptop resources
- Slower on first run (image pulling)
- No usage tracking

### 4.2 Reconnect to TCC

1. Reconnect to Testcontainers Cloud in Desktop app
2. Run the test again
3. Confirm it's running in the cloud

## ✅ Exercise Checklist

- [ ] Installed Testcontainers Desktop
- [ ] Signed up for Testcontainers Cloud
- [ ] Connected Desktop app to TCC
- [ ] Ran first test in the cloud
- [ ] Verified cloud execution indicators
- [ ] Monitored usage in Desktop app
- [ ] Understood free tier limitations
- [ ] Compared local vs cloud execution

## 🚀 Next Steps

Great! You've successfully set up TCC and run your first cloud tests. You're ready for:

- **Exercise 2**: TCC with GitHub Actions
- **Exercise 3**: Real TSE TCC Troubleshooting

## 💡 Key Takeaways

- **TCC Benefits**: No local Docker overhead, consistent environments, usage tracking
- **Free Tier**: 50 minutes/month for cloud execution, unlimited local usage
- **Desktop App**: Essential for local development and usage monitoring
- **Zero Code Changes**: Existing Testcontainers tests work in TCC automatically
