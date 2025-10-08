# Exercise 2: TCC Optimization & Best Practices

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:
- Optimize free tier usage with container sharing
- Implement TCC best practices for efficiency
- Monitor and manage cloud runtime consumption
- Apply optimization techniques to maximize value

## 📚 Prerequisites

- Completed Exercise 1 (TCC Basics)
- Testcontainers Desktop connected to TCC
- Understanding of basic TCC concepts
- Free tier account with remaining minutes

## 🌐 Exercise Overview

This exercise focuses on **maximizing your TCC free tier** and implementing best practices for efficient cloud testing. Learn to optimize container usage and manage your 50 minutes/month effectively.

**Primary Focus**: TCC optimization and efficiency  
**Time**: 30 minutes  
**Key Value**: Maximize free tier usage and learn best practices

## 🚀 Container Sharing Optimization

### Understanding Free Tier Limits

**Free Tier Includes:**
- **50 minutes** of cloud runtime per month
- **No Turbo mode** (parallel execution disabled)
- **Single worker** execution only
- **Desktop usage** counts as "Seats" not minutes

### Optimization Strategy: Container Sharing

**❌ Inefficient Approach:**
```python
# Creates new container per test - wastes cloud minutes!
def test_user_creation():
    with PostgresContainer() as postgres:
        # Test code

def test_user_retrieval():
    with PostgresContainer() as postgres:  # New container!
        # Test code
```

**✅ Efficient Approach:**
```python
# Shares container across tests - saves cloud minutes!
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

## 🧪 Hands-On Optimization

### Python Optimization Example

```bash
# Navigate to Python exercises
cd exercises/python

# Run optimized tests (container sharing)
pytest test_optimized.py -v

# Compare usage in Desktop app
# Notice reduced consumption with container sharing
```

### Java Optimization Example

```java
// This pattern shares containers across tests - saves TCC minutes!
@Testcontainers
class UserRepositoryTest {
    
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15");
    
    // Multiple tests share the same container - efficient!
    @Test
    void shouldCreateUser() { /* ... */ }
    
    @Test  
    void shouldFindUser() { /* ... */ }
}
```

## 📊 Monitoring Usage

### Real-Time Usage Tracking

1. **Testcontainers Desktop**:
   - Monitor usage statistics
   - Track remaining minutes
   - Review consumption patterns

2. **TCC Dashboard**:
   - Check detailed usage reports
   - Analyze consumption trends
   - Plan future usage

### Usage Optimization Tips

**Best Practices:**
- ✅ **Batch related tests** together
- ✅ **Use container sharing** across test classes
- ✅ **Choose efficient base images** (alpine/slim)
- ✅ **Plan test execution** to maximize efficiency
- ✅ **Monitor usage regularly** to avoid surprises

## 🎯 Exercise Checklist

- [ ] ✅ Understand free tier limitations
- [ ] ✅ Implement container sharing in Python
- [ ] ✅ Implement container sharing in Java
- [ ] ✅ Monitor usage in Desktop app
- [ ] ✅ Compare optimized vs unoptimized usage
- [ ] ✅ Learn TCC best practices
- [ ] ✅ Plan efficient test execution

## 🚀 Next Steps

Excellent! You now understand TCC optimization. You're ready for:

- **Exercise 3**: TCC Troubleshooting Scenarios
- **Advanced Topics**: TCC-specific TSE scenarios
- **Production Usage**: Scaling beyond free tier

**Ready for TCC troubleshooting?** Let's move to Exercise 3! 🔧
