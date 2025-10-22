# TSE Investigation Process - The Quota Mystery

## 🔍 Step-by-Step Investigation Guide

### Phase 1: Initial Assessment (5 minutes)

#### 1.1 Review Customer Issue Report
- Read the support ticket details
- Note symptoms: CI pipeline timeout, local works
- Identify timeline: "48 hours ago"
- Check attempted solutions: token regeneration

#### 1.2 Examine GitHub Actions Workflow
```bash
cat customer-report/broken-repo/.github/workflows/test.yml
```
**What to look for:**
- TCC setup action configuration
- Token usage and environment variables
- Workflow structure and dependencies

#### 1.3 Analyze Failure Logs
```bash
cat customer-report/github-actions-logs.txt
```
**Key indicators:**
- Timeout patterns during TCC setup
- Failure timeline correlation
- Network connectivity vs authentication errors

#### 1.4 Run Diagnostic Commands
**Test API connectivity (Mock API is already running):**
```bash
# Test service health
curl http://localhost:8080/v1/health

# Test account access with valid token
curl -H "Authorization: Bearer tcc-lab-token-12345" \
     http://localhost:8080/v1/account

# Check usage and quota status
curl -H "Authorization: Bearer tcc-lab-token-12345" \
     http://localhost:8080/v1/usage
```
**What to look for:**
- Service operational status (200 OK)
- Account plan type and billing model
- Quota usage vs limits
- Authentication success/failure patterns

### Phase 2: Account Investigation (10 minutes)

#### 2.1 Check Account Details
```bash
cat customer-report/account-details.json
```
**Critical information:**
- Account type and plan classification
- Quota usage and limits
- Billing model and restrictions

#### 2.2 Review Usage Dashboard
```bash
cat customer-report/usage-dashboard-screenshot.txt
```
**Key observations:**
- Desktop vs CI/CD usage patterns
- Quota consumption breakdown
- Last successful execution dates

#### 2.3 Verify Billing Model Understanding
**Critical insight:**
- Local execution billing (customer infrastructure)
- CI/CD execution billing (TCC infrastructure)
- Plan type limitations and inclusions

### Phase 3: Root Cause Analysis (10 minutes)

#### 3.1 Identify the Problem
**Root Cause Analysis:**
- Quota exhaustion correlation with failures
- Local vs CI execution differences
- Plan type restrictions

**Supporting evidence:**
- Usage metrics vs limits (from API: 52/50 minutes used)
- Timeline correlation with failures
- Execution environment differences
- API confirmation: `"quota_exceeded": true`

#### 3.2 Understand Customer Confusion
**Common misconceptions:**
- Local usage quota expectations
- Plan type differences
- Billing model complexity

#### 3.3 Plan Type Analysis
**Legacy vs Current Plans:**
- Docker Pro plan differences
- Trial account limitations
- TCC minute inclusions

### Phase 4: Solution Development (15 minutes)

#### 4.1 Immediate Resolution
**Issue explanation:**
- Quota status and limitations
- Local vs CI billing differences
- Plan type restrictions

#### 4.2 Long-term Solutions
**Options for customer:**
1. **Account upgrade**: Enhanced plan with more minutes
2. **Usage optimization**: Reduce CI consumption
3. **Local development**: Unlimited local testing
4. **Alternative approaches**: Hybrid testing strategies

#### 4.3 Customer Education
**Key communication points:**
- Local execution is unlimited (customer infrastructure)
- CI execution counts against quota (TCC infrastructure)
- Plan type differences and inclusions
- Usage optimization strategies

## 📋 Investigation Checklist

- [ ] Reviewed customer issue report and symptoms
- [ ] Examined GitHub Actions workflow configuration
- [ ] Analyzed failure logs and timeline patterns
- [ ] Verified mock TCC API server is running
- [ ] Ran diagnostic curl commands
- [ ] Verified API responses and quota status
- [ ] Checked account type and plan details
- [ ] Verified quota usage and limits
- [ ] Identified local vs CI execution differences
- [ ] Confirmed root cause (quota/billing issue)
- [ ] Developed solution options
- [ ] Prepared customer communication

## 🎯 Success Criteria

**Investigation complete when you can answer:**
1. **Why does local work but CI fails?** (Infrastructure and billing differences)
2. **What changed 48 hours ago?** (Quota exhaustion correlation)
3. **What's the customer's plan type?** (Legacy vs current limitations)
4. **What are the solution options?** (Upgrade, optimize, or alternative approaches)

## 💡 Key Learnings

- **Billing models**: Local vs CI execution has different cost implications
- **Plan types**: Legacy vs current Docker plans have different TCC inclusions
- **Customer confusion**: Billing complexity requires clear communication
- **Investigation process**: Systematic approach from symptoms to resolution
- **Diagnostic tools**: API testing provides concrete evidence for root cause analysis
- **Interactive investigation**: Hands-on testing enhances understanding and confidence
- **Communication**: Technical and business concepts need clear explanation

## 🔧 Diagnostic Tools Reference

**Mock TCC API Server Commands:**
```bash
# Test endpoints (server auto-starts with container)
curl http://localhost:8080/v1/health
curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/account
curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/usage
```

**Expected Key Findings:**
- Service operational (200 OK)
- Quota exceeded: 52/50 minutes
- Plan type: trial_legacy
- Billing model: separate_tcc_billing