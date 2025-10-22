# Investigation Starting Points

## Recommended Investigation Approach

As a TSE, you'll want to follow a systematic troubleshooting methodology:

### 1. Understand the Problem

- Read the customer ticket carefully
- Note the timeline (when did it start?)
- Identify what works vs what doesn't (local vs CI)
- List what customer has already tried

### 2. Gather Evidence

**Check CI Execution Logs:**
```bash
cat customer-data/ci-logs.txt
```
Look for error messages, timeouts, or failure points.

**Review Workflow Configuration:**
```bash
cat customer-data/workflow/test.yml
```
Check for missing steps, misconfigurations, or setup issues.

**Examine Account Information:**
```bash
cat customer-data/account-info.json
```
Verify account status, plan type, and configuration.

**Check Usage Statistics:**
```bash
cat customer-data/usage-data.txt
```
Review usage patterns and any relevant metrics.

### 3. Compare Environments

**Local (Working):**
- Uses Docker Desktop
- Direct container access
- No TCC setup required

**CI (Failing):**
- GitHub Actions runners
- TCC setup in workflow
- Different environment constraints

**Ask yourself:** What's different between these environments?

### 4. Optional: Use TCC Diagnostic API

If you need real-time diagnostics:

```bash
# Start the mock API
cd /workspace/tcc-diagnostic-api
./start-api.sh

# Run diagnostic queries
curl http://localhost:8080/v1/health
curl -H "Authorization: Bearer <token>" http://localhost:8080/v1/account
curl -H "Authorization: Bearer <token>" http://localhost:8080/v1/usage
```

Check the API README for available endpoints and tokens.

### 5. Form Your Hypothesis

Based on evidence gathered:
- What is the root cause?
- Why does local work but CI fails?
- What changed 48 hours ago?

### 6. Verify Your Solution

Once you think you've found the issue:
- Check the `solution/` directory
- Compare your findings with the root cause analysis
- Review the recommended fix

---

## ⚠️ Important Notes

- **Don't jump to conclusions** - Gather all evidence first
- **The answer may not be obvious** - Look carefully at all data
- **Multiple issues may exist** - Identify primary vs secondary causes
- **Documentation matters** - Your customer needs clear explanations

---

## 🎯 Success Criteria

You've successfully completed this exercise when you can:

1. ✅ Identify the root cause with supporting evidence
2. ✅ Explain why local works but CI fails
3. ✅ Recommend the appropriate fix
4. ✅ Draft a professional customer response

Good luck! The customer is waiting.

