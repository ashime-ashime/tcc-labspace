# TCC Diagnostic Techniques

## Common TCC Troubleshooting Areas

When investigating Testcontainers Cloud issues, consider these common problem areas:

### 1. Authentication & Authorization

**Symptoms:**
- "Unauthorized" or "Access denied" errors
- Token validation failures
- Permission issues

**What to Check:**
- Service account token validity
- Token configuration in CI environment
- Token permissions and scopes

### 2. Configuration Issues

**Symptoms:**
- Setup timeouts
- Connection failures
- Workflow configuration errors

**What to Check:**
- GitHub Actions workflow completeness
- TCC setup action presence
- Environment variable configuration
- Network connectivity settings

### 3. Account & Plan Limitations

**Symptoms:**
- Service restrictions
- Access limitations
- Feature unavailability

**What to Check:**
- Account plan type
- Service tier capabilities
- Account status and health
- Usage patterns and consumption

### 4. Environment Differences

**Symptoms:**
- Works locally, fails in CI
- Inconsistent behavior
- Environment-specific errors

**What to Check:**
- Local vs CI environment setup
- Docker Desktop vs TCC differences
- Network connectivity variations
- Resource availability

### 5. Service Health

**Symptoms:**
- Widespread failures
- Timeout issues
- Connectivity problems

**What to Check:**
- TCC service status
- API endpoint availability
- Network latency
- Service degradation

---

## Diagnostic Tools & Commands

### Using the Mock TCC API

The lab includes a mock TCC API for realistic diagnostics:

```bash
# Health Check (no auth required)
curl http://localhost:8080/v1/health

# Account Information (requires auth)
curl -H "Authorization: Bearer <token>" \
     http://localhost:8080/v1/account

# Usage Statistics (requires auth)
curl -H "Authorization: Bearer <token>" \
     http://localhost:8080/v1/usage
```

See `tcc-diagnostic-api/README.md` for tokens and endpoints.

### Analyzing Logs

```bash
# Search for specific errors
grep -i "error" customer-data/ci-logs.txt
grep -i "timeout" customer-data/ci-logs.txt
grep -i "fail" customer-data/ci-logs.txt

# Look for patterns
grep "TCC" customer-data/ci-logs.txt
grep "Testcontainers" customer-data/ci-logs.txt
```

### Checking Configurations

```bash
# View workflow
cat customer-data/workflow/test.yml

# Look for TCC setup
grep -i "testcontainers" customer-data/workflow/test.yml
grep -i "cloud" customer-data/workflow/test.yml
```

---

## Investigation Checklist

Use this checklist to ensure thorough investigation:

- [ ] Read customer ticket completely
- [ ] Review CI execution logs
- [ ] Examine workflow configuration
- [ ] Check account information
- [ ] Review usage statistics
- [ ] Compare local vs CI environments
- [ ] Test connectivity (if applicable)
- [ ] Identify timeline of issue
- [ ] Gather all supporting evidence
- [ ] Form evidence-based hypothesis

---

## 🎯 Best Practices

1. **Be systematic** - Don't skip steps
2. **Document findings** - Take notes as you investigate
3. **Use all available data** - Check every provided file
4. **Think like the customer** - Why would local work but CI fail?
5. **Evidence over assumptions** - Base conclusions on data

---

**Remember:** The most obvious answer isn't always correct. Dig deep!

