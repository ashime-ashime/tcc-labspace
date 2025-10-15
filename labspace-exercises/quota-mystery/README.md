# 🎮 The Quota Mystery - Interactive TSE Investigation Game

## 🕵️‍♂️ Mission Brief

**You are a TSE detective** assigned to solve a critical customer issue. Your mission: investigate why a customer's CI/CD pipeline is failing and propose a solution.

**🎯 Game Features:**
- **Interactive investigation paths** - Choose your own adventure
- **Progressive clue discovery** - Unlock insights as you investigate  
- **Educational insights** - Learn with each finding
- **Scoring system** - Earn points for good detective work
- **Real diagnostic commands** - Practice actual TSE skills

## 🚀 Quick Start - Interactive Mode

```bash
# Start the investigation game
./start-investigation.sh

# Or run the engine directly
python3 .investigation-engine.py
```

## 📋 Traditional Investigation Mode

If you prefer the traditional step-by-step approach:

## 🚨 Customer Issue Report

### Support Ticket Details

**Subject**: GitHub Actions CI pipeline timeout with Testcontainers Cloud

**Priority**: High - Blocking deployments

**Customer**: Enterprise development team

**Description**: 
Our CI/CD pipeline started failing 48 hours ago. The GitHub Actions workflow that sets up Testcontainers Cloud is timing out after approximately 2 minutes. We've attempted to resolve this by regenerating our service account token, but the issue persists.

Our local development environment works perfectly - tests run without issues when executed from developer machines. However, the same tests fail in our GitHub Actions environment.

**Technical Details**:
- Pipeline fails during TCC setup phase
- Timeout occurs before any test execution begins
- No recent changes to our Testcontainers configuration
- Only dependency update was OpenRewrite plugin version bump
- Service account token regeneration had no effect

**Business Impact**: 
This is blocking our deployment pipeline and affecting our release schedule.

## 🕵️ Investigation Mission

As the assigned TSE, you need to:

1. **Analyze the failing CI/CD pipeline**
2. **Determine why local works but CI fails**
3. **Identify the root cause**
4. **Provide actionable solution**

## 🔍 Investigation Process

### Phase 1: Environment Analysis

**Run Diagnostic Commands (Mock API is already running):**
```bash
# Test service health
curl http://localhost:8080/v1/health

# Check quota status
curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/usage

# Verify account details
curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/account
```

Examine the customer's CI configuration:

```bash
cd customer-report/broken-repo
cat .github/workflows/test.yml
```

Review the failure logs:

```bash
cat customer-report/github-actions-logs.txt
```

### Phase 2: Account Investigation

Check account configuration:

```bash
cat customer-report/account-details.json
```

Analyze usage patterns:

```bash
cat customer-report/usage-dashboard-screenshot.txt
```

## 🎯 Key Investigation Areas

### Critical Questions:
1. **What's causing the CI timeout?**
2. **Why does local execution work?**
3. **Is this account-related or configuration-related?**
4. **What changed 48 hours ago?**
5. **Are there billing or quota implications?**

### Diagnostic Approach:

**The mock TCC API server is already running in the background. Use the diagnostic commands above to investigate the issue.**

**Expected Results:**
- **Health**: Service operational (200 OK) - confirms connectivity
- **Usage**: Quota exceeded - 52/50 minutes used - **ROOT CAUSE**
- **Account**: Legacy trial plan with separate TCC billing - explains limitations

## 📋 Investigation Checklist

- [ ] Verified mock TCC API server is running
- [ ] Ran diagnostic curl commands
- [ ] Verified API responses and quota status
- [ ] Analyzed GitHub Actions workflow configuration
- [ ] Reviewed failure logs and error patterns
- [ ] Examined customer account status
- [ ] Checked quota usage and billing information
- [ ] Identified root cause
- [ ] Prepared customer communication
- [ ] Documented resolution steps

## 💡 Investigation Hints

<details>
<summary>Click for hints (use only if stuck)</summary>

**Hint 1**: Focus on account type - legacy vs current billing models

**Hint 2**: Examine usage dashboard data carefully

**Hint 3**: Consider local vs cloud execution differences

**Hint 4**: This may be a quota/billing issue, not technical
</details>

## ✅ Resolution Criteria

Complete when you can:
- Identify the specific cause of CI failures
- Explain local vs CI execution differences
- Understand account limitations
- Provide clear resolution path

## 🚀 Next Exercise

Ready for **Exercise 2: The Connection Mystery**