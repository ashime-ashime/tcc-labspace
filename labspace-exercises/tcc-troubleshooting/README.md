# Exercise 3: TCC Troubleshooting Scenarios

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:
- Diagnose common Testcontainers Cloud issues
- Troubleshoot TCC connectivity problems
- Handle free tier exhaustion scenarios
- Resolve TCC authentication issues
- Apply TCC-specific debugging techniques

## 📚 Prerequisites

- Completed Exercise 1 (TCC Basics)
- Completed Exercise 2 (TCC Optimization)
- Testcontainers Desktop installed and configured
- TCC account with free tier access
- Basic understanding of network troubleshooting

## 🌐 Exercise Overview

This exercise focuses on **real-world TCC troubleshooting scenarios** that TSEs encounter when helping customers. Learn to diagnose and resolve common TCC issues using systematic debugging approaches.

**Primary Focus**: TCC troubleshooting and debugging  
**Time**: 45 minutes  
**Key Value**: TSE-specific problem-solving skills

## 🚨 TCC Connection Issues

### Scenario 1: "No Docker Activity Detected"

**Customer Report**: "My tests aren't running in TCC. Desktop app shows 'No Docker activity detected'."

**Diagnostic Steps**:

1. **Check Testcontainers Desktop Status**:
   ```bash
   # Verify Desktop app is running and connected
   # Look for green "Connected to Testcontainers Cloud" status
   ```

2. **Verify Test Configuration**:
   ```bash
   # Check if tests are actually using Testcontainers
   cd exercises/python
   python3 -c "
   from testcontainers.postgres import PostgresContainer
   print('✅ Testcontainers import successful')
   print('✅ Ready to create containers')
   "
   ```

3. **Test TCC Connection**:
   ```bash
   # Run a simple TCC connectivity test
   ./test-tcc-connection.sh
   ```

**Common Causes & Solutions**:

| Issue | Cause | Solution |
|-------|-------|----------|
| Desktop app not running | User forgot to start app | Start Testcontainers Desktop |
| Not connected to cloud | Network/firewall issues | Check internet connectivity |
| Tests not using Testcontainers | Wrong library/imports | Verify testcontainers imports |
| Authentication failed | Invalid TCC credentials | Re-authenticate in Desktop app |

### Scenario 2: "Tests Running Locally Instead of Cloud"

**Customer Report**: "My tests are running locally instead of in TCC. I want them in the cloud."

**Diagnostic Steps**:

1. **Check Environment Variables**:
   ```bash
   env | grep TESTCONTAINERS
   # Should show TCC-related variables
   ```

2. **Verify Desktop App Configuration**:
   - Check Desktop app settings
   - Ensure "Run with Testcontainers Cloud" is enabled
   - Verify cloud connection status

3. **Test TCC Detection**:
   ```bash
   # Run a test and check for TCC messages
   cd exercises/python
   python3 -m pytest test_user_simple.py::test_user_creation_simple -v -s
   # Look for "testcontainers.cloud" in output
   ```

**Expected TCC Output**:
```
[INFO] Docker host IP address is testcontainers.cloud
[INFO] Running tests with Testcontainers Cloud
```

## 🚨 Performance & Free Tier Issues

### Scenario 3: "Tests Are Too Slow"

**Customer Report**: "My TCC tests are slower than local tests. This doesn't make sense."

**Diagnostic Steps**:

1. **Check First vs Subsequent Runs**:
   ```bash
   # First run (may be slower due to image pulling)
   cd exercises/python
   time python3 -m pytest test_user_simple.py -v
   
   # Second run (should be faster)
   time python3 -m pytest test_user_simple.py -v
   ```

2. **Monitor Container Startup**:
   ```bash
   # Run with verbose output to see timing
   python3 -m pytest test_user_simple.py -v -s
   ```

**Common Causes & Solutions**:

| Issue | Cause | Solution |
|-------|-------|----------|
| First run slow | Image pulling overhead | Normal - subsequent runs faster |
| Network issues | Poor internet connection | Check connectivity |
| Large images | Using heavy base images | Use alpine/slim variants |
| No optimization | Creating new containers per test | Implement container sharing |

### Scenario 4: "Free Tier Exhausted"

**Customer Report**: "I can't run tests anymore. Getting 'quota exceeded' errors."

**Diagnostic Steps**:

1. **Check Usage in Desktop App**:
   - Look for usage statistics
   - Check remaining minutes
   - Review consumption patterns

2. **Monitor Test Execution**:
   ```bash
   # Run tests and monitor usage
   cd exercises/python
   python3 -m pytest test_user_simple.py -v
   # Check Desktop app for updated usage
   ```

**Optimization Techniques**:

```python
# ❌ Inefficient - creates new container per test
def test_user_creation():
    with PostgresContainer() as postgres:
        # Test code

# ✅ Efficient - shares container across tests
@pytest.fixture(scope="class")
def postgres_container():
    with PostgresContainer() as postgres:
        postgres.start()
        yield postgres

class TestUserRepository:
    def test_create_user(self, postgres_container):
        # Reuses same container
```

## 🚨 Authentication & Access Issues

### Scenario 5: "Authentication Failed"

**Customer Report**: "Getting authentication errors when trying to use TCC."

**Diagnostic Steps**:

1. **Check TCC Account Status**:
   - Verify account is active
   - Check for payment issues
   - Confirm free tier eligibility

2. **Test Authentication**:
   ```bash
   # Check if Desktop app can authenticate
   # Look for authentication errors in Desktop app logs
   ```

3. **Re-authenticate**:
   - Sign out of Desktop app
   - Sign back in with valid credentials
   - Verify cloud connection

**Common Causes & Solutions**:

| Issue | Cause | Solution |
|-------|-------|----------|
| Expired credentials | Token/session expired | Re-authenticate in Desktop app |
| Account suspended | Payment/billing issues | Check account status |
| Wrong credentials | Invalid username/password | Verify login credentials |
| Network restrictions | Corporate firewall | Check firewall settings |

## 🔧 TCC-Specific Debugging Techniques

### Debugging Tools & Commands

1. **TCC Environment Check**:
   ```bash
   # Check all TCC-related environment variables
   env | grep -i testcontainer
   env | grep -i docker
   ```

2. **TCC Connectivity Test**:
   ```bash
   # Test TCC API endpoints
   curl -s https://testcontainers.com/cloud/api/health
   curl -s https://testcontainers.com/cloud/api/status
   ```

3. **Container Lifecycle Debugging**:
   ```bash
   # Run tests with verbose output
   python3 -m pytest test_user_simple.py -v -s --tb=long
   
   # Check for TCC-specific messages in output
   python3 -m pytest test_user_simple.py -v | grep -i cloud
   ```

### TCC Log Analysis

**Key Log Messages to Look For**:

```
✅ Good TCC Messages:
- "Docker host IP address is testcontainers.cloud"
- "Running tests with Testcontainers Cloud"
- "Container started in cloud"
- "Connected to Testcontainers Cloud"

❌ Problem Indicators:
- "Connection timeout"
- "Authentication failed"
- "Quota exceeded"
- "Access denied"
- "No Docker activity detected"
```

## 🎯 TSE Troubleshooting Workflow

### Systematic TCC Debugging Process

1. **Gather Information**:
   - Customer's TCC account status
   - Testcontainers Desktop version
   - Operating system and network environment
   - Error messages and logs

2. **Check Basic Requirements**:
   - Desktop app running and connected
   - Internet connectivity
   - Valid TCC account
   - Tests using Testcontainers library

3. **Test Connectivity**:
   - Run TCC connection test
   - Check firewall/proxy settings
   - Verify DNS resolution

4. **Analyze Performance**:
   - Check free tier usage
   - Identify optimization opportunities
   - Recommend container sharing

5. **Provide Solutions**:
   - Step-by-step resolution
   - Optimization recommendations
   - Escalation if needed

## 🎯 Exercise Checklist

- [ ] ✅ Diagnose "No Docker activity detected"
- [ ] ✅ Troubleshoot local vs cloud execution
- [ ] ✅ Handle performance issues
- [ ] ✅ Manage free tier exhaustion
- [ ] ✅ Resolve authentication problems
- [ ] ✅ Debug access denied issues
- [ ] ✅ Apply systematic debugging process
- [ ] ✅ Use TCC-specific debugging tools

## 🚀 Next Steps

Excellent! You now have TCC troubleshooting skills. You're ready for:

- **Real TSE Scenarios**: Handle actual customer TCC tickets
- **Advanced TCC Topics**: CI/CD integration, enterprise features
- **TCC Best Practices**: Production deployment strategies

**Ready to handle TCC tickets like a pro!** 🎯
