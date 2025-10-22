# Exercise 1: CI Pipeline Timeout

## Overview

**Duration:** 20-30 minutes  
**Focus:** GitHub Actions + TCC troubleshooting  
**Type:** Self-directed break-and-fix investigation

## Scenario

A customer's GitHub Actions CI pipeline has been failing for 48 hours. The workflow times out during Testcontainers Cloud setup, but local tests work perfectly. Your mission: investigate and identify the root cause.

## Quick Start

```bash
# 1. Read the customer ticket
cat TICKET.txt

# 2. Investigate customer data
cd customer-data/
ls -la

# 3. Check the logs
cat ci-logs.txt

# 4. Review the workflow
cat workflow/test.yml

# 5. Examine account information
cat account-info.json
cat usage-data.txt
```

## Available Resources

### Customer Data
- `TICKET.txt` - Complete support ticket with customer issue
- `customer-data/` - All files provided by the customer
  - `ci-logs.txt` - GitHub Actions execution logs
  - `account-info.json` - TCC account configuration
  - `usage-data.txt` - TCC usage statistics
  - `workflow/test.yml` - Current GitHub Actions workflow

### Solution Verification
- `solution/` - Check after your investigation
  - `root-cause.md` - Complete root cause analysis
  - `fixed-workflow.yml` - Corrected workflow configuration
  - `customer-response.md` - Professional response template


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

