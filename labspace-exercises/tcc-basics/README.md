# Exercise 1: TCC Basics

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:
- Set up and configure Testcontainers Cloud (TCC)
- Run database tests in the cloud with zero code changes
- Understand TCC benefits over local testing
- Monitor free tier usage effectively

## 📚 Prerequisites

- Testcontainers Desktop installed and configured
- TCC account with free tier (50 minutes/month)
- Internet connectivity for cloud execution
- Basic knowledge of Python or Java

## 🌐 Exercise Overview

This exercise introduces you to **Testcontainers Cloud (TCC)** by running database tests in the cloud instead of locally. You'll experience the benefits of cloud-based testing while learning TCC fundamentals.

**Primary Focus**: Testcontainers Cloud execution  
**Time**: 45 minutes  
**Key Value**: Resource efficiency and consistency

## 🚀 Getting Started

### Step 1: TCC Setup Verification

1. **Check Testcontainers Desktop Status**:
   - Open Testcontainers Desktop
   - Verify status shows **"Connected to Testcontainers Cloud"**
   - Look for green indicator in the app

2. **Test TCC Connection**:
   ```bash
   ./test-tcc-connection.sh
   ```

3. **Expected Output**:
   ```
   ✅ TCC connection successful!
   ✅ Container started: postgresql://test:test@testcontainers.cloud:5432/test
   ```

### Step 2: Monitor Free Tier Usage

1. **Check Usage in Desktop App**:
   - Look for usage statistics
   - Note your remaining cloud minutes
   - Remember: 50 minutes/month free tier

2. **Check TCC Dashboard**:
   - Visit your TCC account dashboard
   - Monitor real-time usage
   - Plan test execution accordingly

## 🧪 Hands-On Exercises

### Python Track: Cloud-Based User Testing

```bash
# Activate Python environment
source venv/bin/activate

# Navigate to Python exercises
cd exercises/python

# Run tests in TCC (automatically uses cloud!)
pytest test_user_simple.py -v
```

**What's Happening:**
- ✅ **Same code** as local testing
- ✅ **Runs in cloud** automatically
- ✅ **No local Docker** overhead
- ✅ **Consistent environment**

### Java Track: Cloud-Based User Testing

```bash
# Navigate to Java exercises
cd exercises/java

# Run tests in TCC (automatically uses cloud!)
mvn test -Dtest=UserRepositorySimpleTest
```

**What's Happening:**
- ✅ **Same Maven command** as local testing
- ✅ **Runs in cloud** automatically
- ✅ **No local Docker daemon** required
- ✅ **Scalable infrastructure**

## 📊 Understanding TCC Benefits

### TCC vs Local Comparison

| Aspect | Local Testcontainers | **Testcontainers Cloud** |
|--------|---------------------|--------------------------|
| **Resource Usage** | Uses your laptop CPU/memory | ✅ **Cloud infrastructure** |
| **Startup Time** | Limited by local hardware | ✅ **Optimized cloud performance** |
| **Consistency** | Varies by machine | ✅ **Same environment for everyone** |
| **Docker Overhead** | Requires local Docker daemon | ✅ **No local Docker needed** |
| **Monitoring** | No built-in usage tracking | ✅ **Real-time usage monitoring** |

## 🎯 Exercise Checklist

- [ ] ✅ Verify Testcontainers Desktop connection
- [ ] ✅ Run TCC connection test successfully
- [ ] ✅ Execute Python tests in TCC
- [ ] ✅ Execute Java tests in TCC
- [ ] ✅ Monitor free tier usage
- [ ] ✅ Understand TCC vs local benefits
- [ ] ✅ Learn container sharing optimization
- [ ] ✅ Identify common TCC troubleshooting steps

## 🚀 Next Steps

Excellent! You now understand Testcontainers Cloud fundamentals. You're ready for:

- **Exercise 2**: TCC Optimization & Best Practices
- **Exercise 3**: TCC Troubleshooting Scenarios
- **Advanced Topics**: TCC-specific TSE scenarios and ticket handling

**Ready for TCC optimization techniques?** Let's move to Exercise 2! 🌐
