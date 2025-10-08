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

## 🚀 Advanced TCC Configuration

### Enterprise Authentication

```bash
# Configure service account with specific permissions
export TESTCONTAINERS_CLOUD_TOKEN="tc_..."
export TESTCONTAINERS_CLOUD_API_URL="https://api.testcontainers.cloud/v1"

# Advanced connection settings
export TESTCONTAINERS_CLOUD_TIMEOUT="300"
export TESTCONTAINERS_CLOUD_RETRY_ATTEMPTS="3"
```

### Performance Optimization

```yaml
# GitHub Actions with advanced TCC settings
- name: Setup TCC with optimization
  uses: atomicjar/testcontainers-cloud-setup-action@v1
  with:
    token: ${{ secrets.TESTCONTAINERS_CLOUD_TOKEN }}
    wait: true
    timeout: 300
    retry-attempts: 3
    retry-delay: 10
```

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
