# TSE Investigation Guide - The Quota Mystery

## 🎯 Lab Overview
**Duration**: 45 minutes  
**Objective**: Diagnose TCC quota exhaustion causing CI/CD failures  
**Skills**: Customer investigation, TCC billing analysis, solution delivery

---

## 📋 Quick Start (2 minutes)
```bash
# Navigate to exercise
cd labspace-exercises/quota-mystery

# Start investigation
cat README.md                    # Read customer ticket
cat tse-investigation/README.md  # Follow investigation guide
```

---

## 🔍 Lab Structure
```
quota-mystery/
├── README.md                    # Customer ticket (START HERE)
├── tse-investigation/           # Investigation guide
│   ├── README.md               # This file
│   └── investigation-steps.md  # Detailed steps
├── customer-report/             # Evidence files
└── solutions/                  # Resolution files
```

---

## 🔍 TSE Investigation Workflow

### Step 1: Read Customer Ticket (5 min)
```bash
cat README.md
```
**What to look for**: Issue description, timeline, business impact

### Step 2: Examine Evidence (15 min)
```bash
# Check broken workflow
cat customer-report/broken-repo/.github/workflows/test.yml

# Review failure logs
cat customer-report/github-actions-logs.txt

# Check account details
cat customer-report/account-details.json

# Analyze usage dashboard
cat customer-report/usage-dashboard-screenshot.txt
```

### Step 3: Identify Root Cause (10 min)
**Key questions**:
- What's causing the CI timeout?
- Why does local work but CI fails?
- Is this account-related or configuration-related?

### Step 4: Develop Solution (10 min)
```bash
# Review working solution
cat solutions/working-solution/test.yml

# Draft customer response
cp solutions/customer-response-template.md my-response.md
```

### Step 5: Complete Investigation (5 min)
**Success criteria**:
- [ ] Root cause identified
- [ ] Solution options developed
- [ ] Customer response drafted

---

## 🛠️ Quick Commands

### Investigation Commands
```bash
# Get overview
head -20 README.md

# Check files
ls -la customer-report/

# Quick file inspection
cat customer-report/account-details.json | grep -E "(quota|usage|exceeded)"
```

### Analysis Commands
```bash
# Compare broken vs working
diff customer-report/broken-repo/.github/workflows/test.yml solutions/working-solution/test.yml

# Check usage patterns
grep -E "(QUOTA|Usage|Status)" customer-report/usage-dashboard-screenshot.txt
```

---

## 📁 File Reference

### Customer Ticket
- `README.md` - Customer issue description

### Evidence Files
- `customer-report/broken-repo/.github/workflows/test.yml` - Broken CI workflow
- `customer-report/github-actions-logs.txt` - Failure logs
- `customer-report/account-details.json` - Account information
- `customer-report/usage-dashboard-screenshot.txt` - Usage data

### Solutions
- `solutions/working-solution/test.yml` - Fixed workflow
- `solutions/customer-response-template.md` - Response template
- `solutions/solution-summary.md` - Resolution summary

### Investigation Guide
- `tse-investigation/investigation-steps.md` - Detailed steps

---

## ✅ Lab Completion Checklist

### Investigation Phase
- [ ] Read customer ticket
- [ ] Examined broken workflow
- [ ] Reviewed failure logs
- [ ] Checked account details
- [ ] Analyzed usage dashboard

### Analysis Phase
- [ ] Identified quota exhaustion (52 > 50 minutes)
- [ ] Understood local vs CI billing differences
- [ ] Recognized legacy plan limitations

### Solution Phase
- [ ] Reviewed working solution
- [ ] Developed resolution options
- [ ] Drafted customer response

### Lab Complete When:
- [ ] Can explain why local works but CI fails
- [ ] Can identify the specific quota issue
- [ ] Can provide clear solution options
- [ ] Can communicate professionally to customer
