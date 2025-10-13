# Exercise 2: The Connection Mystery - A Real TSE Scenario

## 🎯 Learning Objectives

By the end of this exercise, you will:
- Investigate TCC connectivity and authentication issues
- Understand TCC service account and token management
- Diagnose network and configuration problems in TCC
- Handle customer frustration with connection failures
- Practice systematic TSE investigation methodology

## 📚 Prerequisites

- Basic understanding of TCC and authentication concepts
- Familiarity with customer support workflows
- Experience with systematic troubleshooting approaches

## 🚨 The Customer Report

### Initial Support Ticket

> **Subject**: Testcontainers Cloud connection failing - "No Docker activity detected"
> 
> **Description**: Hi, I'm trying to use Testcontainers Cloud but I keep getting "No Docker activity detected" errors. I've followed the setup instructions but it's not working. My tests work fine locally with Docker Desktop, but when I try to use TCC, nothing happens.
> 
> **Steps to Reproduce**:
> 1. Install Testcontainers Desktop
> 2. Sign up for Testcontainers Cloud
> 3. Try to run my tests with TCC
> 4. Get "No Docker activity detected" error
> 
> **Expected Result**: Tests should run in TCC cloud environment
> 
> **Actual Result**: "No Docker activity detected" error, tests don't run in cloud

### Customer Follow-up Information

> The customer reports:
> - Testcontainers Desktop is installed and running
> - Signed up for TCC free trial
> - Tests work perfectly with local Docker Desktop
> - TCC shows "No Docker activity detected"
> - Customer is frustrated and needs this working for their CI/CD pipeline

## 🕵️ Your Investigation Mission

You are the TSE assigned to this case. Your task is to:

1. **Investigate the TCC connection issue**
2. **Analyze the customer's setup and configuration**
3. **Identify why TCC shows "No Docker activity detected"**
4. **Provide solutions to get TCC working properly**

## 🚀 Getting Started

### Step 1: Examine the Customer's Configuration

Navigate to the customer's setup and examine the failing configuration:

```bash
cd customer-report/broken-setup
cat testcontainers-desktop-config.json
cat tcc-connection-logs.txt
```

### Step 2: Analyze the Error Logs

```bash
cat customer-report/error-logs.txt
```

### Step 3: Review Customer's Test Setup

```bash
cat customer-report/broken-setup/simple-test.py
```

### Step 4: Check TCC Account Status

```bash
cat customer-report/account-status.json
```

## 🔍 Investigation Points

### Key Questions to Answer:
1. **Why is TCC showing "No Docker activity detected"?**
2. **What's causing the connection failure between Desktop and TCC?**
3. **Is the customer's TCC account properly configured?**
4. **Are there authentication or token issues?**
5. **What are the common causes of this error?**

### Debugging Approaches:
```bash
# Examine the Desktop configuration
grep -n "cloud\|tcc\|token" customer-report/broken-setup/*.json

# Check connection logs
grep -n "error\|failed\|timeout" customer-report/tcc-connection-logs.txt

# Analyze account status
grep -n "status\|active\|trial" customer-report/account-status.json
```

## 🎯 Expected Learning Outcomes

After completing this exercise, you should understand:
- How to investigate TCC connectivity issues
- The importance of proper TCC account setup and authentication
- Common causes of "No Docker activity detected" errors
- How to troubleshoot TCC Desktop to Cloud connections
- How to communicate technical connectivity issues to customers

## 📋 Investigation Checklist

- [ ] Reviewed customer's TCC setup and configuration
- [ ] Analyzed connection logs and error messages
- [ ] Identified the specific connection failure point
- [ ] Checked TCC account status and authentication
- [ ] Investigated common causes of "No Docker activity detected"
- [ ] Developed solution options
- [ ] Prepared customer response with recommendations

## 💡 Hints

<details>
<summary>Click to reveal hints (use only if stuck)</summary>

**Hint 1**: Check the official TCC documentation at [testcontainers.com/cloud/docs](https://testcontainers.com/cloud/docs/) for troubleshooting "No Docker activity detected" errors.

**Hint 2**: Look at the customer's Testcontainers Desktop configuration - is it properly connected to TCC?

**Hint 3**: Verify the customer's TCC account status and authentication setup.

**Hint 4**: Check if the customer needs to restart Testcontainers Desktop after signing up for TCC.
</details>

## 🎉 Success Criteria

You've successfully completed this exercise when you can:
- Identify the root cause of the "No Docker activity detected" error
- Explain why the customer's TCC connection is failing
- Understand the proper TCC setup and authentication process
- Provide clear solutions to get TCC working
- Communicate the technical issues clearly to the customer

## 🚀 Next Steps

Once you've solved this case, you'll be ready for:
- **Exercise 3**: The CI/CD Mystery
- **Exercise 4**: The Performance Mystery

---

*This exercise is based on real TSE scenarios but all customer details have been anonymized.*
*All solutions reference official Docker TCC documentation at [testcontainers.com/cloud/docs](https://testcontainers.com/cloud/docs/)*