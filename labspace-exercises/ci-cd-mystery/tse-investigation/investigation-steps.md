# TSE Investigation Process - The CI/CD Mystery

## 🔍 Step-by-Step Investigation Guide

### Phase 1: Initial Assessment (5 minutes)

#### 1.1 Review Customer Report
- Read the initial support ticket
- Note the symptoms: "Invalid Service Account Token" in GitHub Actions
- Identify key customer actions: Regenerated token, confirmed active
- Understand customer frustration: CI/CD failing, local works

#### 1.2 Examine GitHub Actions Workflow
```bash
cat customer-report/broken-workflow/.github/workflows/test.yml
```
**What to look for:**
- Correct usage of `atomicjar/testcontainers-cloud-setup-action`
- How the `token` input is passed (`${{ secrets.TESTCONTAINERS_CLOUD_TOKEN }}`)
- Missing TCC setup action
- Token configuration in environment variables
- Any other relevant steps

#### 1.3 Analyze GitHub Actions Logs
```bash
cat customer-report/github-actions-logs.txt
```
**Key indicators:**
- Specific error messages like `Error: Invalid Service Account Token`
- Any warnings or other failures during the TCC setup action
- The exact point of failure in the workflow
- Authentication and connection errors

### Phase 2: Account & Token Deep Dive (10 minutes)

#### 2.1 Check Service Account Status
```bash
cat customer-report/service-account-status.json
```
**What to look for:**
- `status`: Is it `active`?
- `last_used`: When was it last used successfully?
- `permissions`: Does it have the necessary permissions?
- `token_value`: (Simulated) Does it match what the customer *thinks* they copied?

#### 2.2 Verify Token Configuration
- **GitHub Secrets**: Check if token is properly stored in GitHub secrets
- **Token Format**: Verify token starts with `tcct_` prefix
- **Token Length**: Confirm token has correct length
- **Copy-Paste Issues**: Look for leading/trailing whitespace or invisible characters

#### 2.3 Check Workflow Configuration
- **TCC Setup Action**: Verify `atomicjar/testcontainers-cloud-setup-action@v1` is used
- **Token Input**: Check how token is passed to the action
- **Environment Variables**: Verify `TESTCONTAINERS_CLOUD_TOKEN` is set
- **Action Parameters**: Check `wait` and other configuration options

### Phase 3: Root Cause Analysis (15 minutes)

#### 3.1 Synthesize Findings
- **Correlation**: Connect the "Invalid Service Account Token" error with the token value
- **Discrepancy**: Customer regenerated, but still fails. Why?
- **Common Pitfall**: What's a common mistake when copying/pasting tokens?

#### 3.2 Identify Root Cause
- **Primary**: The customer copied the token with leading/trailing whitespace, or an invisible character, making it invalid
- **Secondary**: The token was copied from the wrong place, or an old token was used
- **Tertiary**: GitHub secret configuration issue or action parameter problem

#### 3.3 Understand the Impact
- **Authentication Failure**: TCC setup action cannot authenticate with invalid token
- **Workflow Failure**: GitHub Actions workflow fails at TCC setup step
- **CI/CD Blocking**: Customer's deployment pipeline is blocked

### Phase 4: Solution & Communication (15 minutes)

#### 4.1 Formulate Solution
- **Immediate**: Instruct customer to carefully copy the token again, ensuring no extra characters
- **Verification**: Check GitHub secret configuration
- **Testing**: Rerun GitHub Actions workflow
- **Prevention**: Provide best practices for token handling

#### 4.2 Prepare Customer Response
```bash
cat solutions/customer-response-template.md
```
**Key elements:**
- Clear, empathetic tone
- Concise explanation of the root cause
- Step-by-step instructions for the fix
- Offer further assistance

#### 4.3 Document Solution Summary
```bash
cat solutions/solution-summary.md
```
**Include:**
- Root cause
- Key insights (token handling, common errors)
- Recommended actions
- Lessons learned for future TSE cases

---

## 📚 Key Investigation Points

### Configuration Files to Check
1. **GitHub Actions Workflow**: `.github/workflows/test.yml`
2. **Service Account Status**: Token validity and permissions
3. **GitHub Secrets**: Token storage and configuration
4. **Action Logs**: TCC setup action execution and errors

### Common Issues
1. **Token Copy-Paste Errors**: Leading/trailing whitespace or invisible characters
2. **Missing TCC Setup Action**: Workflow lacks `atomicjar/testcontainers-cloud-setup-action`
3. **Invalid Token Format**: Token doesn't start with `tcct_` or wrong length
4. **GitHub Secret Issues**: Token not properly stored in GitHub secrets

### Troubleshooting Steps
1. **Verify Token**: Check token format and validity
2. **Check GitHub Secrets**: Ensure token is properly stored
3. **Review Workflow**: Confirm TCC setup action is present and configured
4. **Test Authentication**: Verify token works with TCC setup action

---

## 🎯 Expected Outcomes

After following this investigation process, TSEs should be able to:
- Identify the specific token or configuration issue causing the problem
- Understand why the service account token appears valid but fails in CI/CD
- Provide clear, actionable steps to resolve the authentication issue
- Communicate the solution professionally to the customer
- Document the case for future reference and learning
