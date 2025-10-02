# Exercise 4: Testcontainers Cloud Setup

## Learning Objectives

By the end of this exercise, you will be able to:
- Set up and configure Testcontainers Cloud (free tier)
- Understand the benefits of cloud-based container testing
- Configure your tests to use Testcontainers Cloud
- Work within free tier limitations and best practices
- Troubleshoot common Testcontainers Cloud issues

## Prerequisites

- Docker Desktop installed
- Testcontainers Desktop installed
- Basic understanding of Testcontainers (from previous exercises)
- Internet connectivity

## Exercise Overview

In this exercise, you'll learn how to set up and use Testcontainers Cloud within the free tier, which allows you to run your Testcontainers tests in the cloud instead of locally. This provides benefits like better resource management, faster test execution, and reduced local machine resource usage, all while staying within free tier limits.

## Part 1: Understanding Testcontainers Cloud

### What is Testcontainers Cloud?

Testcontainers Cloud is a managed service that runs your Testcontainers tests in cloud environments. Instead of starting containers on your local machine, Testcontainers Cloud:

- Starts containers in cloud infrastructure
- Manages container lifecycle automatically
- Provides better resource isolation
- Reduces local resource usage
- Offers free tier with 50 minutes of cloud runtime

### Benefits of Testcontainers Cloud

1. **Resource Efficiency**: No local Docker daemon overhead
2. **Consistency**: Same environment for all developers
3. **Performance**: Optimized container startup times
4. **Reliability**: Managed infrastructure with high availability
5. **Free Tier**: 50 minutes of cloud runtime for learning and development

## Part 2: Setting Up Testcontainers Cloud

### Step 1: Create Testcontainers Cloud Account

1. Visit [Testcontainers Cloud](https://testcontainers.com/cloud/)
2. Sign up for a free account (includes 50 minutes of cloud runtime)
3. Note your API token from the dashboard
4. Review the free tier limitations in the billing section

### Step 2: Install Testcontainers Desktop

1. Download [Testcontainers Desktop](https://testcontainers.com/desktop/)
2. Install and launch the application
3. Verify Docker Desktop is running and accessible

### Step 3: Configure Testcontainers Cloud in Desktop

1. Open Testcontainers Desktop
2. Go to Settings
3. Enable "Use Testcontainers Cloud"
4. Enter your API token
5. Save settings

### Step 4: Verify Cloud Connection

1. Check the status indicator in Testcontainers Desktop
2. Look for "Connected to Testcontainers Cloud" status
3. Run a simple test to verify cloud execution

## Part 3: Configuring Tests for Testcontainers Cloud

### Java Configuration

#### Basic Cloud Configuration
```java
@Testcontainers
class CloudUserRepositoryTest {
    
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test")
            .withInitScript("init.sql");
    
    @Test
    void shouldCreateUser() {
        // Your test code here
        // Container will run in the cloud automatically
    }
}
```

#### Environment Variable Configuration
```bash
# Set your cloud token
export TC_CLOUD_TOKEN=your_token_here

# Run tests
mvn test
```

#### Programmatic Configuration
```java
@Testcontainers
class CloudTest {
    
    static {
        // Configure cloud settings programmatically
        TestcontainersConfiguration.getInstance()
            .updateGlobalConfig("testcontainers.cloud.token", "your_token_here");
    }
    
    // Your tests here
}
```

### Go Configuration

#### Basic Cloud Configuration
```go
func TestWithCloud(t *testing.T) {
    ctx := context.Background()
    
    postgresContainer, err := postgres.RunContainer(ctx,
        testcontainers.WithImage("postgres:15"),
        postgres.WithDatabase("testdb"),
        postgres.WithUsername("test"),
        postgres.WithPassword("test"),
        postgres.WithInitScripts("init.sql"),
    )
    require.NoError(t, err)
    defer postgresContainer.Terminate(ctx)
    
    // Your test code here
}
```

#### Environment Configuration
```bash
export TC_CLOUD_TOKEN=your_token_here
go test -v
```

### Node.js Configuration

#### Basic Cloud Configuration
```typescript
describe('Cloud UserRepository', () => {
    let postgresContainer: StartedPostgreSqlContainer;
    
    beforeAll(async () => {
        postgresContainer = await new PostgreSqlContainer('postgres:15')
            .withDatabase('testdb')
            .withUsername('test')
            .withPassword('test')
            .withInitScript('init.sql')
            .start();
    });
    
    afterAll(async () => {
        await postgresContainer.stop();
    });
    
    test('should create user in cloud', async () => {
        // Your test code here
    });
});
```

#### Environment Configuration
```bash
export TC_CLOUD_TOKEN=your_token_here
npm test
```

### Python Configuration

#### Basic Cloud Configuration
```python
import pytest
from testcontainers.postgres import PostgresContainer

class TestCloudUserRepository:
    
    @pytest.fixture(scope="class")
    def postgres_container(self):
        with PostgresContainer("postgres:15") as postgres:
            postgres.with_database("testdb")
            postgres.with_username("test")
            postgres.with_password("test")
            postgres.with_init_script("init.sql")
            yield postgres
    
    def test_create_user_in_cloud(self, postgres_container):
        # Your test code here
        pass
```

#### Environment Configuration
```bash
export TC_CLOUD_TOKEN=your_token_here
pytest -v
```

## Part 4: Free Tier Best Practices

### Understanding Free Tier Limitations

The Testcontainers Cloud free tier includes:
- **50 minutes** of cloud runtime per month
- **Single worker** environment (no parallel execution)
- **Basic support** through community channels
- **Standard container images** (no custom registries)

### Optimizing Free Tier Usage

#### 1. Efficient Test Design
```java
@Testcontainers
class OptimizedCloudTest {
    
    // Use static containers to share across test methods
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test")
            .withInitScript("init.sql");
    
    @Test
    void shouldCreateUser() {
        // Test runs efficiently in shared container
    }
    
    @Test
    void shouldUpdateUser() {
        // Reuses the same container instance
    }
}
```

#### 2. Container Reuse Strategies
```java
// Use @Testcontainers annotation for class-level container sharing
@Testcontainers
class UserRepositoryTest {
    
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15");
    
    @BeforeEach
    void setUp() {
        // Clean up data between tests, not containers
        userRepository.deleteAllUsers();
    }
    
    // Multiple tests share the same container
}
```

#### 3. Minimize Container Startup Time
```java
// Use smaller, faster images
static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:13-alpine")
    .withDatabaseName("testdb")
    .withUsername("test")
    .withPassword("test");

// Pre-pull images locally to speed up cloud startup
// docker pull postgres:13-alpine
```

#### 4. Optimize Test Data
```java
@Test
void shouldCreateMultipleUsers() {
    // Create multiple users in one test instead of separate tests
    List<User> users = Arrays.asList(
        new User("user1", "user1@example.com"),
        new User("user2", "user2@example.com"),
        new User("user3", "user3@example.com")
    );
    
    for (User user : users) {
        User created = userRepository.createUser(user);
        assertThat(created.getId()).isNotNull();
    }
}
```

### Monitoring Free Tier Usage

#### Track Your Usage
1. **Dashboard Monitoring:**
   - Check Testcontainers Cloud dashboard regularly
   - Monitor remaining minutes
   - Review usage patterns

2. **Local Development Strategy:**
   ```java
   // Use local Docker for development
   @Testcontainers
   class DevelopmentTest {
       
       @Container
       static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
           .withReuse(true); // Reuse containers locally
   }
   
   // Use cloud only for CI/CD or final validation
   ```

#### Usage Optimization Tips

1. **Batch Related Tests:**
   ```java
   @Test
   void shouldHandleCompleteUserWorkflow() {
       // Test create, read, update, delete in one test
       User user = userRepository.createUser(new User("test", "test@example.com"));
       User found = userRepository.findById(user.getId());
       found.setEmail("updated@example.com");
       userRepository.updateUser(found);
       userRepository.deleteUser(found.getId());
   }
   ```

2. **Use Efficient Cleanup:**
   ```java
   @BeforeEach
   void setUp() {
       // Quick cleanup instead of container restart
       userRepository.deleteAllUsers();
   }
   ```

3. **Minimize External Dependencies:**
   ```java
   // Use lightweight containers
   static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:13-alpine");
   
   // Avoid complex multi-container setups in free tier
   ```

## Part 5: Advanced Cloud Configuration

### Custom Cloud Settings

#### Java Configuration
```java
@Testcontainers
class AdvancedCloudTest {
    
    static {
        // Configure cloud settings for free tier
        TestcontainersConfiguration.getInstance()
            .updateGlobalConfig("testcontainers.cloud.token", "your_token")
            .updateGlobalConfig("testcontainers.cloud.enabled", "true");
    }
    
    // Your tests here
}
```

### Environment-Specific Configuration

#### Development vs Production
```java
public class CloudConfig {
    
    public static void configureForEnvironment() {
        String environment = System.getProperty("test.environment", "development");
        
        if ("production".equals(environment)) {
            // Production settings - use cloud for CI/CD
            TestcontainersConfiguration.getInstance()
                .updateGlobalConfig("testcontainers.cloud.enabled", "true");
        } else {
            // Development settings - use local Docker to save cloud minutes
            TestcontainersConfiguration.getInstance()
                .updateGlobalConfig("testcontainers.cloud.enabled", "false");
        }
    }
}
```

### CI/CD Integration

#### GitHub Actions
```yaml
name: Test with Testcontainers Cloud

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up JDK 11
      uses: actions/setup-java@v3
      with:
        java-version: '11'
        distribution: 'temurin'
    
    - name: Run tests with Testcontainers Cloud
      env:
        TC_CLOUD_TOKEN: ${{ secrets.TC_CLOUD_TOKEN }}
      run: mvn test
```

#### Jenkins Pipeline
```groovy
pipeline {
    agent any
    
    environment {
        TC_CLOUD_TOKEN = credentials('tc-cloud-token')
    }
    
    stages {
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
    }
}
```

## Part 6: Monitoring and Debugging

### Cloud Activity Monitoring

1. **Testcontainers Desktop Dashboard:**
   - View running containers
   - Monitor resource usage
   - Check connection status

2. **Cloud Dashboard:**
   - View usage statistics
   - Monitor billing
   - Check service status

### Debugging Cloud Issues

#### Enable Verbose Logging
```java
// Java
System.setProperty("testcontainers.cloud.debug", "true");
System.setProperty("testcontainers.cloud.verbose", "true");
```

```bash
# Environment variables
export TC_CLOUD_DEBUG=true
export TC_CLOUD_VERBOSE=true
```

#### Common Debugging Steps
1. Check cloud connection status
2. Verify API token validity
3. Monitor container startup logs
4. Check network connectivity
5. Review usage quotas

### Performance Monitoring

#### Measuring Performance
```java
@Test
void performanceTest() {
    long startTime = System.currentTimeMillis();
    
    // Your test code here
    
    long endTime = System.currentTimeMillis();
    long duration = endTime - startTime;
    
    System.out.println("Test completed in: " + duration + "ms");
    
    // Assert reasonable performance
    assertThat(duration).isLessThan(30000); // 30 seconds
}
```

## Part 7: Best Practices

### Cloud Testing Best Practices

1. **Resource Management:**
   - Use appropriate container sizes
   - Implement proper cleanup
   - Monitor resource usage

2. **Test Organization:**
   - Group related tests together
   - Use meaningful test names
   - Implement proper test isolation

3. **Configuration Management:**
   - Use environment-specific settings
   - Store sensitive data securely
   - Version control configuration files

4. **Performance Optimization:**
   - Use container reuse when possible
   - Optimize initialization scripts
   - Monitor test execution times

### Security Considerations

1. **Token Management:**
   - Store tokens securely
   - Rotate tokens regularly
   - Use environment variables

2. **Network Security:**
   - Use secure connections
   - Implement proper access controls
   - Monitor network traffic

## Exercise Checklist

Complete the following tasks:

- [ ] Set up Testcontainers Cloud free tier account
- [ ] Install and configure Testcontainers Desktop
- [ ] Enable cloud mode in Testcontainers Desktop
- [ ] Configure tests to use Testcontainers Cloud
- [ ] Run basic tests in cloud environment
- [ ] Implement free tier optimization strategies
- [ ] Set up container reuse for efficiency
- [ ] Monitor cloud usage and remaining minutes
- [ ] Set up environment-specific configurations
- [ ] Implement proper error handling and debugging
- [ ] Test CI/CD integration (optional)
- [ ] Document cloud configuration for your team

## Troubleshooting

### Common Cloud Issues

1. **Authentication Failures:**
   - Verify API token is correct
   - Check token hasn't expired
   - Ensure proper environment variable setup

2. **Connection Issues:**
   - Check internet connectivity
   - Verify firewall settings
   - Test cloud service availability

3. **Performance Issues:**
   - Monitor resource usage
   - Check for rate limiting
   - Optimize container configurations

4. **Billing Issues:**
   - Monitor usage in dashboard
   - Check quota limits
   - Review billing settings

## Next Steps

After completing this exercise:
1. Integrate Testcontainers Cloud into your existing test suites
2. Configure your CI/CD pipelines to use cloud testing
3. Train your team on cloud testing best practices
4. Monitor and optimize cloud usage
5. Explore advanced cloud features and integrations

## Learning Reflection

Consider these questions:
1. What are the main benefits of using Testcontainers Cloud within the free tier?
2. How does cloud testing differ from local testing?
3. When would you choose cloud testing over local testing?
4. How can you optimize cloud testing to stay within free tier limits?
5. What strategies can you use to maximize the value of your 50 free minutes?
6. What security considerations are important for cloud testing?
