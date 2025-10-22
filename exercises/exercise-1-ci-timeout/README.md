# Exercise 1: CI Pipeline Timeout

## Overview

**Duration:** 20-30 minutes  
**Focus:** GitHub Actions + TCC troubleshooting  
**Type:** Self-directed break-and-fix investigation

## Scenario

A customer's GitHub Actions CI pipeline has been failing for 48 hours. The workflow times out during Testcontainers Cloud setup, but local tests work perfectly. Your mission: investigate and identify the root cause.

## Investigation Steps

**📋 For detailed step-by-step instructions, see: `TSE-GUIDE.md`**

**Follow these steps to complete your TSE analysis:**

### **Step 1: Read the Customer Ticket**
```bash
cat TICKET.txt
```

### **Step 2: Investigate Customer Data**
```bash
cd customer-data/
ls -la

# Check the CI logs
cat ci-logs.txt

# Review the workflow configuration
cat workflow/test.yml

# Examine account information
cat account-info.json
cat usage-data.txt
```

### **Step 3: Analyze the Issue**
- Review all customer data thoroughly
- Identify patterns and inconsistencies
- Form your hypothesis about the root cause

### **Step 4: Submit Your Analysis**
```bash
# Run the analysis script
./analyze-issue.sh
```

**The script will ask you:**
1. Your name (for tracking)
2. What you think is the root cause
3. What solution you recommend

**Your analysis will be saved automatically with your name and timestamp for instructor review.**

## Available Resources

### Customer Data
- `TICKET.txt` - Complete support ticket with customer issue
- `customer-data/` - All files provided by the customer
  - `ci-logs.txt` - GitHub Actions execution logs
  - `account-info.json` - TCC account configuration
  - `usage-data.txt` - TCC usage statistics
  - `workflow/test.yml` - Current GitHub Actions workflow

### Analysis Submission
- `analyze-issue.sh` - Interactive script to submit your analysis
- Your analysis will be saved automatically with timestamp and your name


## Investigation Tips

1. **Read the ticket thoroughly** - Understand what works vs what fails
2. **Check logs first** - Error messages often point to the issue
3. **Review configurations** - Look for missing or incorrect setup
4. **Examine account details** - Verify the customer's environment
5. **Compare environments** - Why does local work but CI fails?
6. **Don't assume** - Gather all evidence before concluding

## Success Criteria

You've successfully completed this exercise when you can:

✅ Identify the root cause with supporting evidence  
✅ Explain why local works but CI fails  
✅ Recommend the appropriate fix  
✅ Draft a professional customer response  

## What You'll Learn

- Systematic TCC troubleshooting methodology
- GitHub Actions workflow configuration
- TCC account and plan limitations
- Environment parity debugging
- Professional customer communication

---

**Ready to investigate? The customer is waiting for your analysis.**

