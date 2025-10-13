# TSE Investigation Process

## 🔍 Step-by-Step Investigation Guide

### Phase 1: Initial Assessment (5 minutes)

#### 1.1 Review Customer Report
- Read the initial support ticket
- Note the symptoms: CI failing, local working
- Identify timeline: "since 2 days ago"
- Check if token regeneration was attempted

#### 1.2 Examine GitHub Actions Workflow
```bash
cat customer-report/broken-repo/.github/workflows/test.yml
```
**What to look for:**
- Proper TCC setup action usage
- Token configuration
- Workflow structure

#### 1.3 Analyze Failure Logs
```bash
cat customer-report/github-actions-logs.txt
```
**Key indicators:**
- Timeout waiting for connection
- Pattern of failures since specific date
- No network or auth errors

### Phase 2: Account Investigation (10 minutes)

#### 2.1 Check Account Details
```bash
cat customer-report/account-details.json
```
**Critical information:**
- Account type: `legacy_trial`
- Plan type: `trial_legacy`
- Quota status: `quota_exceeded: true`
- Usage: `52 minutes` vs `50 minute limit`

#### 2.2 Review Usage Dashboard
```bash
cat customer-report/usage-dashboard-screenshot.txt
```
**Key observations:**
- Desktop usage: 0 minutes (Local - Unlimited)
- CI/CD usage: 52 minutes (Cloud - Quota Exceeded)
- Last successful CI: 2025-01-08
- Quota exhausted: 2025-01-09

#### 2.3 Verify Billing Model Understanding
**Critical insight:**
- Local usage is unlimited (runs on customer's machine)
- CI/CD usage counts against quota
- Legacy trial: 50 minutes one-time, not monthly

### Phase 3: Root Cause Analysis (10 minutes)

#### 3.1 Identify the Problem
**Root Cause:** Quota exhaustion on legacy trial account

**Supporting evidence:**
- Usage: 52 minutes > 50 minute limit
- Timeline: Failures started when quota was hit
- Local works because it's unlimited
- CI fails because it's quota-limited

#### 3.2 Understand Customer Confusion
**Customer misconceptions:**
- Thinks local usage should count against quota
- Expects monthly quota reset (legacy was 300 min/month)
- Doesn't understand legacy vs new plan differences
- Confused by "Local" usage in dashboard

#### 3.3 Plan Type Analysis
**Legacy vs New Plans:**
- Legacy Docker Pro: No TCC minutes included
- New Docker Pro: 100 TCC minutes included
- Legacy trial: 50 minutes one-time
- New trial: 50 minutes one-time

### Phase 4: Solution Development (15 minutes)

#### 4.1 Immediate Resolution
**Explain the issue:**
- Quota exhaustion (52 > 50 minutes)
- Local vs CI billing differences
- Legacy plan limitations

#### 4.2 Long-term Solutions
**Options for customer:**
1. **Wait for quota reset**: Not applicable (one-time quota)
2. **Upgrade to new Docker Pro**: Get 100 minutes/month
3. **Optimize tests**: Reduce CI usage
4. **Use local testing**: Unlimited for development

#### 4.3 Customer Education
**Key points to communicate:**
- Local usage is unlimited (your machine)
- CI usage counts against quota (TCC infrastructure)
- Legacy plans don't include TCC minutes
- New consolidated plans include TCC minutes

## 📋 Investigation Checklist

- [ ] Reviewed customer ticket and symptoms
- [ ] Examined GitHub Actions workflow
- [ ] Analyzed failure logs and timeline
- [ ] Checked account type and plan details
- [ ] Verified quota usage and limits
- [ ] Identified local vs CI billing differences
- [ ] Confirmed root cause (quota exhaustion)
- [ ] Developed solution options
- [ ] Prepared customer communication

## 🎯 Success Criteria

**You've successfully investigated when you can answer:**
1. **Why does local work but CI fails?** (Local unlimited, CI quota-limited)
2. **What changed 2 days ago?** (Quota was exhausted)
3. **What's the customer's plan type?** (Legacy trial, 50 min one-time)
4. **What are the solution options?** (Upgrade, optimize, or use local)

## 💡 Key Learnings

- **Quota models**: Local vs CI usage is billed differently
- **Plan types**: Legacy vs new Docker plans have different TCC inclusions
- **Customer confusion**: Billing models are complex and poorly documented
- **Investigation process**: Systematic approach from symptoms to root cause
- **Communication**: Clear explanation of technical and billing concepts
