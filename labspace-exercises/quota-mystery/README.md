# Exercise 1: The Quota Mystery - A Real TSE Scenario

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Investigate complex TCC quota and billing issues
- Understand legacy vs new Docker plan differences
- Diagnose local vs CI usage billing models
- Handle customer confusion about quota limits
- Practice systematic TSE investigation methodology

## 📚 Prerequisites

- Basic understanding of TCC and GitHub Actions
- Familiarity with Docker billing models
- Experience with customer support workflows

## 🚨 The Customer Report

### Initial Support Ticket
> **Subject**: Testcontainers Cloud not working in GitHub Actions
> 
> **Description**: Hi, since 2 days the GitHub Action to set-up Testcontainers Cloud in our pipelines is failing with a timeout. We've tried to regenerate the service account token but it still fails. You can see an example of an affected repository here: [customer-repo-example]
> 
> Please, can you help me in figuring out what is going wrong?
> 
> Thanks!

### Customer Follow-up Information
> The customer reports:
> - Tests work perfectly from their local machine
> - GitHub Actions timeout after 2 minutes
> - No recent changes to Testcontainers setup
> - Only a Maven dependency version bump (OpenRewrite plugin)
> - Error happens before any Maven command runs
> - Regenerated service account token with no effect

## 🕵️ Your Investigation Mission

You are the TSE assigned to this case. Your task is to:

1. **Investigate the failing GitHub Actions**
2. **Understand why local works but CI fails**
3. **Identify the root cause**
4. **Provide a clear solution to the customer**

## 🚀 Getting Started

### Step 1: Examine the Customer's Environment

Navigate to the customer's repository and examine the failing workflow:

```bash
cd customer-report/broken-repo
cat .github/workflows/test.yml
```

### Step 2: Analyze the GitHub Actions Logs

```bash
cat customer-report/github-actions-logs.txt
```

### Step 3: Check TCC Account Status

```bash
# Examine the customer's account information
cat customer-report/account-details.json
```

### Step 4: Review Usage Dashboard

```bash
cat customer-report/usage-dashboard-screenshot.txt
```

## 🔍 Investigation Points

### Key Questions to Answer:
1. **Why does local testing work but CI fails?**
2. **What changed 2 days ago?**
3. **Is this a quota/billing issue?**
4. **Are there multiple accounts or orgs involved?**
5. **What's the customer's current plan type?**

### Diagnostic Commands:
```bash
# Check TCC API health
curl https://api.testcontainers.cloud/v1/health

# Verify service account token (if available)
curl -H "Authorization: Bearer $TOKEN" \
     https://api.testcontainers.cloud/v1/health

# Check quota status
curl -H "Authorization: Bearer $TOKEN" \
     https://api.testcontainers.cloud/v1/usage
```

## 🎯 Expected Learning Outcomes

After completing this exercise, you should understand:
- How to systematically investigate TCC quota issues
- The difference between legacy and new Docker plans
- Why local vs CI usage is billed differently
- How to handle customer confusion about billing models
- When and how to escalate complex account issues

## 📋 Investigation Checklist

- [ ] Reviewed customer's GitHub Actions workflow
- [ ] Analyzed failure logs and error messages
- [ ] Checked customer's TCC account status
- [ ] Verified quota usage and limits
- [ ] Identified root cause of the issue
- [ ] Prepared customer response with solution
- [ ] Documented investigation findings

## 💡 Hints

<details>
<summary>Click to reveal hints (use only if stuck)</summary>

**Hint 1**: Check the customer's account type - are they on a legacy or new plan?

**Hint 2**: Look at the usage dashboard carefully - what type of usage is shown?

**Hint 3**: Consider the difference between local and CI usage billing.

**Hint 4**: The issue might be related to quota limits, not technical configuration.
</details>

## 🎉 Success Criteria

You've successfully completed this exercise when you can:
- Identify that the customer hit their quota limit
- Explain why local works but CI fails
- Understand the legacy plan limitations
- Provide clear next steps for the customer

## 🚀 Next Steps

Once you've solved this case, you'll be ready for:
- **Exercise 2**: The Authentication Nightmare
- **Exercise 3**: The Performance Mystery

---

*This exercise is based on real TSE scenarios but all customer details have been anonymized.*
