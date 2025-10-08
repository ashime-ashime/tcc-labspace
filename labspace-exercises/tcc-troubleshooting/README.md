# Exercise 3: Advanced TSE TCC Troubleshooting and Enterprise Scenarios

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Handle complex enterprise TCC integration issues
- Diagnose advanced networking and authentication problems
- Troubleshoot multi-environment TCC deployments
- Provide sophisticated customer support solutions for enterprise clients

## 📚 Prerequisites

- Completed Exercise 1 (TCC Architecture)
- Completed Exercise 2 (Enterprise CI/CD Integration)
- Deep understanding of TCC infrastructure and billing models
- Experience with enterprise networking and security protocols

## 🚨 Real TSE Scenarios

These scenarios are based on actual customer tickets and TSE experiences.

## 🎭 Scenario 1: "My Tests Work Locally But Fail in CI"

### Customer Report
> "I can run my tests locally with Testcontainers Desktop, but they fail in GitHub Actions with timeout errors. Why does local work but CI doesn't?"

### 🕵️ TSE Investigation Process

#### Step 1: Gather Information
Ask the customer for:
- GitHub Actions workflow configuration
- Error messages and logs
- TCC account type (free vs paid)
- When the issue started

#### Step 2: Check Quota Status
```bash
# Access TCC dashboard
# Check current month usage
# Verify quota remaining
```

#### Step 3: Analyze the Issue
**Root Cause**: Free tier quota exhaustion
- **Local Desktop**: Unlimited usage (runs on customer's machine)
- **CI/CD**: Counts against 50-minute monthly quota
- **Customer Confusion**: Different billing for local vs cloud

#### Step 4: Provide Solution
1. **Immediate Fix**: Explain quota exhaustion
2. **Long-term**: Suggest plan upgrade or optimization
3. **Education**: Clarify local vs CI billing differences

### 📋 TSE Response Template
```
Hi [Customer],

Thanks for reaching out about your TCC CI issues. I can help you resolve this.

The issue is that your TCC free tier quota (50 minutes/month) has been exhausted. 
Here's why local works but CI doesn't:

• Local Desktop usage: Unlimited (runs on your machine)
• CI/CD usage: Counts against your 50-minute quota

I've checked your account and you've used 52 minutes this month.

Solutions:
1. Wait until next month for quota reset
2. Upgrade to Docker Pro ($5/month) for 100 minutes
3. Optimize tests with container sharing

Let me know if you'd like help with any of these options.

Best regards,
[TSE Name]
```

## 🎭 Scenario 2: "I Got a Quota Notification But Tests Still Work"

### Customer Report
> "I received a notification saying I ran out of TCC minutes, but my tests are still working on my laptop. Is this a bug?"

### 🕵️ TSE Investigation

#### Step 1: Understand the Confusion
**Customer Misunderstanding**: Thinks quota applies to all usage

#### Step 2: Check Account Details
- Verify customer's plan type
- Check quota usage breakdown
- Confirm local vs cloud usage

#### Step 3: Explain the Billing Model
```
Local Desktop (unlimited):
• Tests run on your machine
• No quota consumption
• Shows as "Local" in dashboard

CI/CD Cloud (quota applies):
• Tests run in TCC infrastructure  
• Consumes quota minutes
• Shows as "Cloud" in dashboard
```

### 📋 TSE Response Template
```
Hi [Customer],

The notification is correct - you've exhausted your cloud quota, but local usage 
is unlimited. This is working as designed:

• ✅ Local Desktop: Unlimited usage (your machine)
• ❌ CI/CD Cloud: 50 minutes/month quota

Your tests work locally because they're not consuming cloud minutes.
CI/CD tests would fail due to quota exhaustion.

This is the expected behavior. Would you like to upgrade your plan 
for more cloud minutes?

Best regards,
[TSE Name]
```

## 🎭 Scenario 3: "TCC Agent Setup Fails in GitHub Actions"

### Customer Report
> "My GitHub Action keeps failing when setting up the TCC agent. I regenerated the token but it still doesn't work."

### 🕵️ TSE Investigation Process

#### Step 1: Verify Setup
Check customer's workflow:
```yaml
- name: Set up Testcontainers Cloud
  uses: atomicjar/testcontainers-cloud-setup-action@v1
  with:
    token: ${{ secrets.TESTCONTAINERS_CLOUD_TOKEN }}
```

#### Step 2: Common Issues to Check
1. **Token Format**: Extra spaces, incorrect secret name
2. **Service Account**: Inactive or expired
3. **Quota**: Exhausted cloud minutes
4. **Network**: Firewall or proxy issues

#### Step 3: Diagnostic Commands
```bash
# Test token validity
curl -H "Authorization: Bearer $TOKEN" \
     https://api.testcontainers.cloud/v1/health

# Check quota status
curl -H "Authorization: Bearer $TOKEN" \
     https://api.testcontainers.cloud/v1/usage
```

### 📋 TSE Response Template
```
Hi [Customer],

Let's troubleshoot your TCC GitHub Actions setup step by step:

1. Verify your token is correctly set in GitHub secrets
2. Check that your service account is active
3. Confirm you have remaining quota minutes

Can you run this diagnostic command in your workflow?
```yaml
- name: Test TCC Connection
  run: |
    curl -H "Authorization: Bearer ${{ secrets.TESTCONTAINERS_CLOUD_TOKEN }}" \
         https://api.testcontainers.cloud/v1/health
```

Also, please share:
• Your GitHub Actions workflow file
• The exact error message
• Screenshot of your TCC dashboard usage

This will help me identify the specific issue.

Best regards,
[TSE Name]
```

## 🎭 Scenario 4: "Legacy Docker Pro Plan Doesn't Include TCC"

### Customer Report
> "I have a Docker Pro subscription but TCC is still charging me. Shouldn't it be included?"

### 🕵️ TSE Investigation

#### Step 1: Check Plan Type
- Verify if customer has legacy vs new Docker Pro plan
- Legacy plans (pre-2024) don't include TCC minutes
- New consolidated plans include TCC

#### Step 2: Explain Plan Differences
```
Legacy Docker Pro:
• Docker Hub features
• No TCC minutes included
• Separate TCC billing

New Docker Pro:
• Docker Hub features  
• 100 TCC minutes included
• Consolidated billing
```

### 📋 TSE Response Template
```
Hi [Customer],

I've checked your account and you have a legacy Docker Pro subscription 
that doesn't include TCC minutes. Here's what changed:

Legacy Plans (your current):
• Docker Hub features only
• TCC billed separately (50 min free tier)

New Consolidated Plans:
• Docker Hub + TCC included
• 100 TCC minutes/month
• $5/month for Pro

Your options:
1. Keep current plan + use TCC free tier
2. Upgrade to new consolidated plan
3. Purchase additional TCC minutes

Would you like me to help you upgrade to the new plan?

Best regards,
[TSE Name]
```

## 🔧 TSE Troubleshooting Toolkit

### Essential Commands
```bash
# Check TCC health
curl https://api.testcontainers.cloud/v1/health

# Verify token (replace TOKEN)
curl -H "Authorization: Bearer TOKEN" \
     https://api.testcontainers.cloud/v1/health

# Check usage
curl -H "Authorization: Bearer TOKEN" \
     https://api.testcontainers.cloud/v1/usage
```

### Key Questions to Ask Customers
1. What's your current Docker/TCC plan?
2. When did the issue start?
3. Are you using Desktop app or CI/CD?
4. What's your current quota usage?
5. Can you share error messages/logs?

### Common Solutions
1. **Quota Issues**: Upgrade plan or wait for reset
2. **Auth Problems**: Regenerate service account token
3. **CI Failures**: Check token format and quota
4. **Billing Confusion**: Explain local vs cloud usage

## ✅ Exercise Checklist

- [ ] Handled quota exhaustion scenario
- [ ] Explained local vs CI billing differences
- [ ] Troubleshot GitHub Actions setup
- [ ] Resolved legacy plan confusion
- [ ] Applied systematic troubleshooting
- [ ] Used proper TSE response templates
- [ ] Understood customer communication best practices

## 🚀 Congratulations!

You've completed all three TCC exercises and are now ready to handle real TSE scenarios with confidence!

## 💡 Key TSE Takeaways

- **Quota Management**: 50 minutes/month is strict for CI
- **Billing Education**: Local vs cloud usage is confusing for customers
- **Systematic Approach**: Gather info → Diagnose → Provide solution
- **Customer Communication**: Clear explanations and actionable solutions
- **Plan Knowledge**: Understand legacy vs new Docker plans