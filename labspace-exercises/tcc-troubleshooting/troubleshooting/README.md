# TCC Troubleshooting Guide

This guide helps you resolve common issues encountered while working with **Testcontainers Cloud (TCC)** in this lab.

## 🎯 TCC-First Approach

This lab is designed exclusively for **Testcontainers Cloud**. All testing happens in the cloud - no local Docker required.

## Table of Contents

1. [TCC Setup Issues](#tcc-setup-issues)
2. [TCC Connection Issues](#tcc-connection-issues)
3. [TCC Performance Issues](#tcc-performance-issues)
4. [TCC Free Tier Issues](#tcc-free-tier-issues)
5. [Local Fallback](#local-fallback)
6. [Getting Additional Help](#getting-additional-help)

## TCC Setup Issues

### Testcontainers Desktop Not Running

**Symptoms:**
- Tests run locally instead of in cloud
- "No Docker activity detected" messages
- Missing TCC connection status

**Solutions:**
1. **Start Testcontainers Desktop**:
   - Download from [testcontainers.com/cloud](https://testcontainers.com/cloud/)
   - Install and launch the application
   - Verify "Connected to Testcontainers Cloud" status

2. **Check Desktop App Status**:
   - Look for green indicator in Desktop app
   - Verify cloud connection is active
   - Check for any error messages

3. **Restart if needed**:
   - Close and reopen Testcontainers Desktop
   - Sign out and sign back in
   - Verify account status

### TCC Authentication Issues

**Symptoms:**
- "Authentication failed" errors
- Cannot connect to TCC
- "Invalid credentials" messages

**Solutions:**
1. **Verify Account Status**:
   - Check TCC account is active
   - Verify free tier eligibility
   - Confirm account hasn't expired

2. **Re-authenticate**:
   - Sign out of Desktop app
   - Sign back in with valid credentials
   - Check for account confirmation emails

3. **Check Token Status**:
   - Verify API token is valid
   - Check token hasn't expired
   - Regenerate token if needed

## TCC Connection Issues

### "Tests Running Locally Instead of Cloud"

**Symptoms:**
- Tests execute on local Docker
- Missing TCC messages in output
- Desktop app shows no activity

**Diagnostic Steps:**
```bash
# Check environment variables
env | grep TESTCONTAINERS

# Test TCC detection
cd exercises/python
python3 -m pytest test_user_simple.py -v -s
# Look for "testcontainers.cloud" in output
```

**Expected TCC Output:**
```
[INFO] Docker host IP address is testcontainers.cloud
[INFO] Running tests with Testcontainers Cloud
```

**Solutions:**
- Restart Testcontainers Desktop
- Re-enable cloud mode in settings
- Check firewall/proxy settings
- Verify TCC account status

### Network Connectivity Issues

**Symptoms:**
- "Connection timeout" errors
- Cannot reach TCC endpoints
- Tests hanging during startup

**Diagnostic Steps:**
```bash
# Test TCC connectivity
curl -I https://testcontainers.com/cloud/
curl -I https://testcontainers.com/cloud/api/health

# Check DNS resolution
nslookup testcontainers.com
nslookup testcontainers.cloud
```

**Solutions:**
1. **Check Internet Connection**:
   - Verify internet connectivity
   - Test other websites
   - Check for network outages

2. **Firewall/Proxy Issues**:
   - Configure firewall to allow TCC domains
   - Set up proxy configuration if needed
   - Use corporate VPN if required

3. **DNS Issues**:
   - Try different DNS servers (8.8.8.8, 1.1.1.1)
   - Clear DNS cache
   - Check corporate DNS restrictions

## TCC Performance Issues

### "Tests Are Too Slow"

**Symptoms:**
- TCC tests slower than expected
- Long container startup times
- Timeout errors

**Diagnostic Steps:**
```bash
# Test first vs subsequent runs
cd exercises/python
time python3 -m pytest test_user_simple.py -v
time python3 -m pytest test_user_simple.py -v
```

**Common Causes & Solutions:**

| Issue | Cause | Solution |
|-------|-------|----------|
| First run slow | Image pulling overhead | Normal - subsequent runs faster |
| Network issues | Poor internet connection | Check connectivity speed |
| Large images | Heavy base images | Use alpine/slim variants |
| No optimization | New containers per test | Implement container sharing |

**Optimization Techniques:**
```python
# ✅ Efficient - shares container across tests
@pytest.fixture(scope="class")
def postgres_container():
    with PostgresContainer("postgres:15-alpine") as postgres:
        postgres.start()
        yield postgres

class TestUserRepository:
    def test_create_user(self, postgres_container):
        # Reuses same container - efficient!
        
    def test_find_user(self, postgres_container):
        # Reuses same container - saves cloud minutes!
```

## TCC Free Tier Issues

### "Free Tier Exhausted"

**Symptoms:**
- "Quota exceeded" errors
- Cannot run tests
- Usage limit reached

**Diagnostic Steps:**
```bash
# Check usage in Desktop app
# Monitor consumption patterns
# Review test execution frequency
```

**Solutions:**
1. **Monitor Usage**:
   - Check Desktop app for usage statistics
   - Track remaining minutes
   - Review consumption patterns

2. **Optimize Container Usage**:
   ```python
   # Container sharing saves minutes
   @pytest.fixture(scope="class")
   def shared_container():
       # Share across multiple tests
   ```

3. **Strategic Usage**:
   - Use local Docker for development
   - Use TCC only for final validation
   - Batch related tests together
   - Use smaller, faster images

### Free Tier Optimization

**Best Practices:**
- **Container Sharing**: Reuse containers across tests
- **Efficient Images**: Use alpine/slim variants
- **Batch Testing**: Group related tests together
- **Cloud Development**: Use TCC for all testing

## TCC Requirements

### Pure Cloud Approach

**This lab requires TCC because:**
- ✅ **No local Docker needed** - Everything runs in cloud
- ✅ **Consistent environment** - Same for all developers
- ✅ **Resource efficiency** - No local machine overhead
- ✅ **Cloud-native experience** - Learn modern testing practices

**TCC Prerequisites:**
- ✅ Internet connectivity
- ✅ Testcontainers Desktop app
- ✅ TCC account (free tier available)
- ✅ No corporate firewall blocking TCC

## Getting Additional Help

### TCC Debugging Tools

1. **Testcontainers Desktop**:
   - Monitor container lifecycle
   - View usage statistics
   - Check connection status
   - Debug authentication issues

2. **TCC Connection Test**:
   ```bash
   # Run TCC connectivity test
   ./test-tcc-connection.sh
   ```

3. **Environment Check**:
   ```bash
   # Check TCC configuration
   env | grep -i testcontainer
   ```

### TCC Status Messages

**✅ Good TCC Messages:**
```
- "Docker host IP address is testcontainers.cloud"
- "Running tests with Testcontainers Cloud"
- "Container started in cloud"
- "Connected to Testcontainers Cloud"
```

**❌ Problem Indicators:**
```
- "Connection timeout"
- "Authentication failed"
- "Quota exceeded"
- "Access denied"
- "No Docker activity detected"
```

### Community Resources

- [Testcontainers Cloud Documentation](https://testcontainers.com/cloud/docs/)
- [Testcontainers Slack](https://slack.testcontainers.org/)
- [GitHub Discussions](https://github.com/testcontainers/testcontainers-java/discussions)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/testcontainers)

### Lab Support

For lab-specific TCC issues:
1. Check this troubleshooting guide
2. Review [TCC Common Issues](COMMON_ISSUES.md)
3. Run `./test-tcc-connection.sh` for diagnostics
4. Contact lab instructors
5. Check TCC account status and usage

## 🎯 Pure TCC Philosophy

Remember: This lab is **exclusively Testcontainers Cloud** because:
- ✅ **Resource efficiency** - No local Docker overhead
- ✅ **Consistency** - Same environment for all developers  
- ✅ **Scalability** - Cloud infrastructure handles load
- ✅ **Real-world experience** - TCC is the future of containerized testing
- ✅ **Pure cloud experience** - Learn modern cloud-native testing

**No local Docker needed** - Pure TCC learning experience! 🌐