# Exercise 2: Enterprise TCC CI/CD Integration and Advanced Troubleshooting

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Implement TCC in complex enterprise CI/CD pipelines
- Diagnose advanced TCC integration issues
- Understand TCC billing models and quota management
- Handle enterprise authentication and network configurations

## 📚 Prerequisites

- Completed Exercise 1 (TCC Architecture)
- Advanced GitHub Actions and CI/CD experience
- Enterprise authentication system knowledge
- Understanding of container orchestration and networking

## 🚨 Real TSE Scenario: GitHub Actions TCC Timeout

### Customer Issue
> "Hi, since 2 days the GitHub Action to set-up Testcontainers Cloud in our pipelines is failing with a timeout. We've tried to regenerate the service account token but it still fails."

### What We'll Learn
This exercise is based on a real customer ticket. You'll learn to diagnose and resolve the most common TCC GitHub Actions issues.

## 🚀 Step 1: Set Up TCC Service Account

### 1.1 Create Service Account

1. Go to [Testcontainers Cloud](https://testcontainers.com/cloud/)
2. Sign in to your account
3. Navigate to "Service Accounts"
4. Click "Create Service Account"
5. Give it a name (e.g., "github-actions")
6. Copy the generated token

### 1.2 Add Token to GitHub Secrets

In your GitHub repository:
1. Go to Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `TESTCONTAINERS_CLOUD_TOKEN`
4. Value: (paste your service account token)
5. Click "Add secret"

## 🧪 Step 2: Configure GitHub Actions Workflow

### 2.1 Create Basic Workflow

Create `.github/workflows/test.yml`:

```yaml
name: Test with TCC

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Set up Java
      uses: actions/setup-java@v4
      with:
        java-version: '17'
        
    - name: Cache Maven dependencies
      uses: actions/cache@v3
      with:
        path: ~/.m2
        key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
        
    - name: Set up Testcontainers Cloud
      uses: atomicjar/testcontainers-cloud-setup-action@v1
      with:
        wait: true
        token: ${{ secrets.TESTCONTAINERS_CLOUD_TOKEN }}
        
    - name: Run tests
      run: mvn test
```

### 2.2 Test the Workflow

1. Commit and push your changes
2. Go to Actions tab in GitHub
3. Watch the workflow run
4. Check for TCC connection success

## 🔧 Step 3: Troubleshoot Common Issues

### 3.1 Issue: Timeout Waiting for Connection

**Symptoms:**
```
Error: Timeout waiting for Testcontainers Cloud connection
```

**Diagnostic Steps:**

1. **Check Token Validity:**
   ```bash
   # Verify token is correctly set
   echo $TESTCONTAINERS_CLOUD_TOKEN
   ```

2. **Check Quota Status:**
   - Log into Testcontainers Cloud dashboard
   - Check remaining minutes
   - Verify you haven't hit the 50-minute limit

3. **Verify Service Account:**
   - Ensure service account is active
   - Check token hasn't expired
   - Regenerate if needed

### 3.2 Issue: Authentication Failed

**Symptoms:**
```
Error: Authentication failed for Testcontainers Cloud
```

**Solutions:**

1. **Regenerate Service Account Token:**
   - Delete old token
   - Create new service account
   - Update GitHub secret

2. **Check Token Format:**
   - Ensure no extra spaces or characters
   - Copy token exactly as generated

### 3.3 Issue: Quota Exceeded

**Symptoms:**
```
Error: Quota exceeded for Testcontainers Cloud
```

**Understanding the Issue:**
- **Free Tier**: 50 minutes/month for ALL cloud usage
- **CI Usage**: Counts against your quota (unlike local Desktop usage)
- **Legacy vs New Plans**: Different quota structures

**Solutions:**

1. **Check Usage Dashboard:**
   - Monitor current month usage
   - Identify high-consumption tests

2. **Optimize Test Execution:**
   ```yaml
   # Use container sharing to reduce usage
   - name: Run tests with optimization
     run: mvn test -Dtestcontainers.reuse.enable=true
   ```

3. **Upgrade Plan:**
   - Consider Docker Pro/Team plans
   - Get more TCC minutes

## 🎯 Step 4: Advanced Troubleshooting

### 4.1 Debug Connection Issues

Add debugging to your workflow:

```yaml
- name: Debug TCC Connection
  run: |
    echo "Testing TCC connectivity..."
    curl -H "Authorization: Bearer ${{ secrets.TESTCONTAINERS_CLOUD_TOKEN }}" \
         https://api.testcontainers.cloud/v1/health
```

### 4.2 Monitor Usage in CI

```yaml
- name: Check TCC Usage
  run: |
    echo "Checking current TCC usage..."
    # Add usage monitoring commands
```

### 4.3 Handle Flaky Connections

```yaml
- name: Set up Testcontainers Cloud with retry
  uses: atomicjar/testcontainers-cloud-setup-action@v1
  with:
    wait: true
    token: ${{ secrets.TESTCONTAINERS_CLOUD_TOKEN }}
    retry-attempts: 3
    retry-delay: 10
```

## 📊 Step 5: Real Customer Resolution

### 5.1 The Actual Issue (from the ticket)

The customer's problem was:
1. **Quota Exhaustion**: Hit the 50-minute free tier limit
2. **Confusion**: Local Desktop usage doesn't count against quota, but CI does
3. **Legacy Plan**: Old Docker Pro subscription didn't include TCC minutes

### 5.2 TSE Resolution Steps

1. **Verify Quota Status**: Checked customer's usage dashboard
2. **Explain Billing**: Clarified local vs CI usage differences  
3. **Plan Upgrade**: Recommended upgrading to new Docker plan
4. **Optimization**: Suggested container sharing techniques

### 5.3 Key Learnings

- **Free Tier Limits**: 50 minutes/month is strict
- **Usage Types**: Local Desktop ≠ CI usage for billing
- **Legacy Plans**: Old subscriptions may not include TCC
- **Customer Confusion**: Many don't understand the billing model

## ✅ Exercise Checklist

- [ ] Created TCC service account
- [ ] Added token to GitHub secrets
- [ ] Configured basic GitHub Actions workflow
- [ ] Successfully ran tests in TCC
- [ ] Troubleshot timeout issues
- [ ] Handled authentication problems
- [ ] Understood quota limitations
- [ ] Learned real customer resolution

## 🚀 Next Steps

Excellent! You've mastered TCC in GitHub Actions. You're ready for:

- **Exercise 3**: Real TSE TCC Troubleshooting

## 💡 Key Takeaways

- **Service Accounts**: Required for CI/CD integration
- **Quota Management**: 50 minutes/month is strict for CI
- **Authentication**: Tokens must be properly configured
- **Troubleshooting**: Most issues are quota or auth-related
- **Customer Support**: Understanding billing is crucial for TSEs
