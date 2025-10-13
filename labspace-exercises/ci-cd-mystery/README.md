# Exercise 3: The CI/CD Mystery - A Real TSE Scenario

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Investigate TCC CI/CD integration and GitHub Actions failures
- Understand TCC service account setup and token management
- Diagnose environment differences between local and CI environments
- Handle customer frustration with CI/CD pipeline failures
- Practice systematic TSE investigation methodology

## 📚 Prerequisites

- Basic understanding of TCC and GitHub Actions
- Familiarity with CI/CD pipeline concepts
- Experience with customer support workflows

## 🚨 The Customer Report

### Initial Support Ticket

> **Subject**: GitHub Actions failing with TCC - "Service account authentication failed"
> 
> **Description**: Hi, I'm trying to use Testcontainers Cloud in my GitHub Actions workflow, but it keeps failing with "Service account authentication failed" errors. The same tests work perfectly when I run them locally with Testcontainers Desktop, but they fail in CI.
> 
> **Steps to Reproduce**:
> 1. Run tests locally with Testcontainers Desktop → ✅ Works
> 2. Push to GitHub and trigger CI workflow → ❌ Fails
> 3. Check GitHub Actions logs → "Service account authentication failed"
> 
> **Expected Result**: Tests should run in TCC cloud environment via GitHub Actions
> 
> **Actual Result**: "Service account authentication failed" error in CI

### Customer Follow-up Information

> The customer reports:
> - Local tests work perfectly with Testcontainers Desktop
> - GitHub Actions workflow fails with authentication errors
> - Service account token is configured in GitHub Secrets
> - TCC account is active and has quota remaining
> - Customer needs this working for their CI/CD pipeline

## 🕵️ Your Investigation Mission

You are the TSE assigned to this case. Your task is to:

1. **Investigate the TCC CI/CD authentication failure**
2. **Analyze the customer's GitHub Actions workflow and configuration**
3. **Identify why authentication works locally but fails in CI**
4. **Provide solutions to get TCC working in GitHub Actions**

## 🚀 Getting Started

### Step 1: Examine the Customer's GitHub Actions Workflow

Navigate to the customer's workflow and examine the failing configuration:

```bash
cd customer-report/broken-workflow
cat .github/workflows/test.yml
```

### Step 2: Analyze the GitHub Actions Logs

```bash
cat customer-report/github-actions-logs.txt
```

### Step 3: Review Customer's TCC Configuration

```bash
cat customer-report/tcc-config.json
```

### Step 4: Check Service Account Status

```bash
cat customer-report/service-account-status.json
```

## 🔍 Investigation Points

### Key Questions to Answer:
1. **Why does authentication work locally but fail in CI?**
2. **What's causing the "Service account authentication failed" error?**
3. **Is the service account token properly configured in GitHub Actions?**
4. **Are there environment differences between local and CI?**
5. **What are the common causes of TCC CI/CD authentication failures?**

### Debugging Approaches:
```bash
# Examine the GitHub Actions workflow
grep -n "testcontainers\|TCC\|token" customer-report/broken-workflow/.github/workflows/test.yml

# Check authentication configuration
grep -n "TESTCONTAINERS_CLOUD_TOKEN\|secrets" customer-report/broken-workflow/.github/workflows/test.yml

# Analyze service account status
grep -n "status\|active\|token" customer-report/service-account-status.json
```

## 🎯 Expected Learning Outcomes

After completing this exercise, you should understand:
- How to investigate TCC CI/CD authentication issues
- The importance of proper service account configuration in GitHub Actions
- Common causes of "Service account authentication failed" errors
- How to troubleshoot TCC integration in CI/CD pipelines
- How to communicate technical CI/CD issues to customers

## 📋 Investigation Checklist

- [ ] Reviewed customer's GitHub Actions workflow configuration
- [ ] Analyzed CI/CD logs and error messages
- [ ] Identified the specific authentication failure point
- [ ] Checked service account status and token configuration
- [ ] Investigated environment differences between local and CI
- [ ] Developed solution options
- [ ] Prepared customer response with recommendations

## 💡 Hints

<details>
<summary>Click to reveal hints (use only if stuck)</summary>

**Hint 1**: Check the official TCC documentation at [testcontainers.com/cloud/docs](https://testcontainers.com/cloud/docs/) for GitHub Actions integration troubleshooting.

**Hint 2**: Look at the customer's GitHub Actions workflow - is the TCC setup action properly configured?

**Hint 3**: Verify the service account token configuration in GitHub Secrets.

**Hint 4**: Check if the customer needs to use the TCC agent in their CI workflow.
</details>

## 🎉 Success Criteria

You've successfully completed this exercise when you can:
- Identify the root cause of the "Service account authentication failed" error
- Explain why authentication works locally but fails in CI
- Understand the proper TCC CI/CD setup and configuration process
- Provide clear solutions to get TCC working in GitHub Actions
- Communicate the technical CI/CD issues clearly to the customer

## 🚀 Next Steps

Once you've solved this case, you'll be ready for:
- **Exercise 4**: The Performance Mystery

---

*This exercise is based on real TSE scenarios but all customer details have been anonymized.*
*All solutions reference official Docker TCC documentation at [testcontainers.com/cloud/docs](https://testcontainers.com/cloud/docs/)*
