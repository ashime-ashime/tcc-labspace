# Exercise 1: TCC Setup and First Tests

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Set up Testcontainers Desktop and connect to TCC
- Run your first tests in Testcontainers Cloud
- Understand the difference between local and cloud execution
- Monitor your TCC usage

## 📚 Prerequisites

- Docker Desktop installed and running
- Internet connectivity
- Basic understanding of testing concepts

## 🚀 Step 1: Install Testcontainers Desktop

### 1.1 Download Testcontainers Desktop

Visit [https://testcontainers.com/desktop/](https://testcontainers.com/desktop/) and download the app for your OS:

- **Mac**: `brew install atomicjar/tap/testcontainers-desktop`
- **Windows**: Download the Windows installer
- **Linux**: Download .deb or .rpm package

### 1.2 Install and Start the App

```bash
# For Mac with Homebrew
brew install atomicjar/tap/testcontainers-desktop

# Start the app
testcontainers-desktop
```

### 1.3 Sign Up for Testcontainers Cloud

1. Open Testcontainers Desktop
2. Click "Sign up for free"
3. Create your account
4. Sign in to the app

**Expected Result**: You should see "Connected to Testcontainers Cloud" in the app.

## 🧪 Step 2: Run Your First TCC Test

### 2.1 Create a Simple Test

Let's create a basic test that runs in TCC:

```bash
# Navigate to the Python example
cd python

# Install dependencies
pip install testcontainers[postgres] psycopg2-binary pytest

# Run the test
pytest test_simple.py -v
```

### 2.2 What Should Happen

When you run the test, you should see:
- Testcontainers Desktop shows activity
- Tests run in the cloud (not locally)
- Your laptop resources are preserved
- Test completes successfully

### 2.3 Verify Cloud Execution

Look for these indicators that tests are running in TCC:
- Testcontainers Desktop shows "Cloud" activity
- No local Docker containers created
- Faster startup times after first run
- Usage tracking in the Desktop app

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
