# TSE Exercise Guide - CI Pipeline Timeout

## Your Mission
Investigate a customer's failing CI pipeline and identify the root cause.

---

## Step-by-Step Instructions

### STEP 1: Navigate to the Exercise
```bash
cd exercises/exercise-1-ci-timeout
ls -la
```

**This navigates you to the exercise directory and shows you what files are available.**

### STEP 2: Read the Customer Issue
```bash
cat TICKET.txt
```

**This displays the customer support ticket with the problem description.**

### STEP 3: Investigate Customer Data
```bash
cd customer-data/
ls -la
```

**This takes you into the customer data directory and shows all available files.**

**Check each file:**

```bash
cat ci-logs.txt
```

**This displays the GitHub Actions execution logs.**

```bash
cat workflow/test.yml
```

**This shows the current GitHub Actions workflow configuration.**

```bash
cat account-info.json
```

**This displays the TCC account configuration and details.**

```bash
cat usage-data.txt
```

**This shows the TCC usage statistics and patterns.**

### STEP 4: Think Through Your Analysis

**Ask yourself:**
- What patterns do you see across all files?
- What's different between local vs CI?
- What could be causing the timeout?
- What evidence supports your hypothesis?

### STEP 5: Submit Your Analysis
```bash
cd ..
./analyze-issue.sh
```

**This runs the analysis script that will collect your findings.**

**The script will ask:**
1. Your name
2. Root cause
3. Solution

---

## Success Criteria

You're done when:
- You've read the customer ticket
- You've investigated all customer data files
- You've analyzed the patterns
- You've run the analysis script
- Your analysis file has been created

---

## Investigation Tips

- Look for patterns across all files
- Compare local vs CI environments
- Don't assume - gather evidence
- Read carefully for important clues
- Think systematically

---

## Files You'll Find

- `TICKET.txt` - Customer support ticket
- `customer-data/ci-logs.txt` - GitHub Actions logs
- `customer-data/account-info.json` - TCC account info
- `customer-data/usage-data.txt` - TCC usage stats
- `customer-data/workflow/test.yml` - GitHub Actions workflow

---

**Remember: Investigate thoroughly before running the analysis script!**
