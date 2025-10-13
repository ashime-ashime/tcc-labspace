# Customer Response Template - TCC CI/CD Authentication Issue

## 📧 TSE Response to Customer

---

**Subject: Re: GitHub Actions failing with TCC - "Service account authentication failed"**

Hi [Customer Name],

Thanks for reaching out about your TCC CI/CD authentication issue. I've investigated your case and can help you resolve this "Service account authentication failed" error.

## 🔍 Root Cause Analysis

The issue is that your GitHub Actions workflow is missing the TCC setup action. Here's what I found:

**Current Configuration:**
- Service account token is properly configured in GitHub Secrets ✅
- Token is valid and active ✅
- TCC account has quota remaining ✅
- **Missing**: TCC setup action in your GitHub Actions workflow ❌

**Why You're Getting "Service account authentication failed":**
- Your workflow has the token but doesn't set up the TCC agent
- Tests try to connect to TCC without the agent being configured
- The TCC agent is required to authenticate with the cloud service

## 🚀 Solution

Here's how to fix your GitHub Actions workflow:

### Step 1: Add TCC Setup Action

Add this step to your `.github/workflows/test.yml` **before** running tests:

```yaml
- name: Set up Testcontainers Cloud
  uses: atomicjar/testcontainers-cloud-setup-action@v1
  with:
    wait: true
    token: ${{ secrets.TESTCONTAINERS_CLOUD_TOKEN }}
```

### Step 2: Complete Updated Workflow

Here's your complete fixed workflow:

```yaml
name: Test with Testcontainers Cloud

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
      
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install testcontainers[postgres] psycopg2-binary pytest
        
    - name: Set up Testcontainers Cloud
      uses: atomicjar/testcontainers-cloud-setup-action@v1
      with:
        wait: true
        token: ${{ secrets.TESTCONTAINERS_CLOUD_TOKEN }}
        
    - name: Run tests
      run: python -m pytest tests/ -v
```

### Step 3: Test Your Updated Workflow

1. **Commit and push** your updated workflow
2. **Trigger the workflow** by pushing to your repository
3. **Check the logs** - you should see TCC agent setup and successful test execution

## 📚 Understanding the Issue

**What Happened:**
- You correctly configured the service account token in GitHub Secrets
- However, your workflow was missing the TCC setup action
- The TCC agent needs to be configured before tests can authenticate

**Why This Happens:**
- TCC requires an agent to be set up in CI environments
- The service account token alone isn't sufficient
- The setup action configures the agent to authenticate with TCC

**Local vs CI Difference:**
- **Local**: Testcontainers Desktop handles TCC authentication automatically
- **CI**: Requires explicit TCC agent setup via the setup action

## 🔧 Verification Steps

After following the solution, you should see:
- ✅ TCC setup action completes successfully
- ✅ Tests run in TCC cloud environment
- ✅ No more "Service account authentication failed" errors
- ✅ Your TCC dashboard shows CI usage activity

## 📖 Reference Documentation

For more information, see the official TCC documentation:
- [TCC for CI Documentation](https://testcontainers.com/cloud/docs/)
- [GitHub Actions Integration](https://testcontainers.com/cloud/docs/)
- [TCC Setup Action](https://testcontainers.com/cloud/docs/)

## 📞 Support and Follow-up

I've provided you with the updated workflow configuration that includes the required TCC setup action. This should resolve the "Service account authentication failed" error and get your tests running in TCC via GitHub Actions.

**Next Steps:**
1. Update your workflow with the TCC setup action
2. Commit and push the changes
3. Monitor the workflow execution
4. Let me know if you encounter any issues

If you need help with any of these steps or encounter any issues, please don't hesitate to reach out. I'm here to help you get TCC working properly in your CI/CD pipeline!

Best regards,
[TSE Name]
Docker Support

---

## 📋 Response Checklist

- [ ] Acknowledged customer's TCC CI/CD authentication issue
- [ ] Explained root cause (missing TCC setup action)
- [ ] Provided specific solution with complete workflow
- [ ] Explained why this issue occurs
- [ ] Provided verification steps
- [ ] Referenced official TCC documentation
- [ ] Offered ongoing support and follow-up
- [ ] Used professional, helpful tone

## 💡 Key Communication Points

1. **Be empathetic**: Customer is frustrated with CI/CD failures
2. **Be specific**: Provide complete workflow configuration
3. **Be educational**: Help customer understand local vs CI differences
4. **Be supportive**: Offer ongoing assistance and follow-up
5. **Be practical**: Focus on actionable solution steps

## 🎯 Expected Customer Reaction

**Positive outcomes:**
- Customer understands the missing TCC setup action
- Customer successfully updates their workflow
- Customer's CI/CD pipeline starts working with TCC
- Customer feels supported and educated

**Follow-up actions:**
- Monitor customer's workflow updates
- Provide additional guidance if needed
- Document case for future reference
- Share learnings with team about common TCC CI/CD issues
