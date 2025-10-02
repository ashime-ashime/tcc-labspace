# Troubleshooting Guide

This guide helps you resolve common issues encountered while working with Docker Testcontainers in this lab.

## Table of Contents

1. [Setup Issues](#setup-issues)
2. [Container Issues](#container-issues)
3. [Database Connection Issues](#database-connection-issues)
4. [Test Execution Issues](#test-execution-issues)
5. [Performance Issues](#performance-issues)
6. [Language-Specific Issues](#language-specific-issues)
7. [Testcontainers Cloud Issues](#testcontainers-cloud-issues)

## Setup Issues

### Docker Desktop Not Running

**Symptoms:**
- Tests fail with connection errors
- Testcontainers can't start containers
- Error: "Docker daemon not running"

**Solutions:**
1. Start Docker Desktop application
2. Verify Docker is running: `docker ps`
3. Check Docker Desktop settings and ensure it's properly configured
4. Restart Docker Desktop if needed

### Port Conflicts

**Symptoms:**
- Container startup failures
- "Port already in use" errors
- Tests hanging during container startup

**Solutions:**
```bash
# Check what's using a port
lsof -i :5432  # PostgreSQL
lsof -i :3306  # MySQL
lsof -i :6379  # Redis
lsof -i :5672  # RabbitMQ

# Kill processes if necessary
kill -9 <PID>

# Use different ports in your tests
postgres.withExposedPorts(5433)  # Java
```

### Permission Issues (Linux/macOS)

**Symptoms:**
- "Permission denied" when accessing Docker
- Cannot start containers

**Solutions:**
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Log out and back in for changes to take effect
# Or restart your terminal session

# Verify permissions
docker ps
```

## Container Issues

### Container Startup Timeout

**Symptoms:**
- Tests timeout waiting for containers to start
- "Container did not start within timeout" errors

**Solutions:**
1. **Increase timeout:**
   ```java
   // Java
   postgres.withStartupTimeout(Duration.ofMinutes(5))
   ```

   ```go
   // Go
   postgres.WithWaitStrategy(wait.ForLog("ready to accept connections").
       WithStartupTimeout(5 * time.Minute))
   ```

2. **Check system resources:**
   - Ensure sufficient RAM and CPU available
   - Close unnecessary applications
   - Check Docker Desktop resource allocation

3. **Use different base images:**
   - Try lighter images (e.g., `postgres:13-alpine`)
   - Avoid images with large download sizes

### Container Not Ready

**Symptoms:**
- Tests fail immediately after container starts
- Database connection errors despite container running

**Solutions:**
1. **Add proper wait strategies:**
   ```java
   // Java - Wait for specific log message
   postgres.waitingFor(Wait.forLogMessage("ready to accept connections", 1))
   ```

   ```go
   // Go - Wait for port to be available
   postgres.WithWaitStrategy(wait.ForListeningPort("5432/tcp"))
   ```

2. **Verify initialization scripts:**
   - Check SQL scripts are valid
   - Ensure scripts don't have syntax errors
   - Verify file paths are correct

### Container Cleanup Issues

**Symptoms:**
- Containers not being removed after tests
- Resource exhaustion over time
- "Too many containers" errors

**Solutions:**
1. **Ensure proper cleanup:**
   ```java
   // Java - Use @Testcontainers annotation
   @Testcontainers
   class MyTest {
       @Container
       static PostgreSQLContainer<?> postgres = ...
   }
   ```

2. **Manual cleanup:**
   ```bash
   # Remove all stopped containers
   docker container prune
   
   # Remove unused images
   docker image prune
   
   # Remove all unused resources
   docker system prune
   ```

## Database Connection Issues

### Connection Refused

**Symptoms:**
- "Connection refused" errors
- Cannot connect to database container

**Solutions:**
1. **Check connection parameters:**
   ```java
   // Java - Use container's JDBC URL
   String jdbcUrl = postgres.getJdbcUrl();
   ```

2. **Verify container is ready:**
   ```java
   // Wait for container to be ready
   postgres.waitingFor(Wait.forLogMessage("ready to accept connections", 1))
   ```

3. **Check network connectivity:**
   - Ensure containers are on the same network
   - Verify port mappings are correct

### Authentication Failures

**Symptoms:**
- "Authentication failed" errors
- "Invalid username/password" messages

**Solutions:**
1. **Verify credentials:**
   ```java
   postgres.withUsername("test")
           .withPassword("test")
   ```

2. **Check database configuration:**
   - Ensure database name is correct
   - Verify user has proper permissions

### Database Not Initialized

**Symptoms:**
- Tables don't exist
- Schema not created
- Initialization scripts not running

**Solutions:**
1. **Check initialization scripts:**
   ```java
   postgres.withInitScript("init.sql")
   ```

2. **Verify script location:**
   - Ensure scripts are in the correct path
   - Check file permissions
   - Validate SQL syntax

3. **Use file-based initialization:**
   ```java
   postgres.withCopyFileToContainer(
       MountableFile.forClasspathResource("init.sql"),
       "/docker-entrypoint-initdb.d/init.sql"
   )
   ```

## Test Execution Issues

### Tests Running Slowly

**Symptoms:**
- Tests take a long time to complete
- Container startup is slow

**Solutions:**
1. **Use container reuse:**
   ```java
   // Java - Reuse containers across test classes
   @Testcontainers(disabledWithoutDocker = true)
   class MyTest {
       @Container
       static PostgreSQLContainer<?> postgres = ...
   }
   ```

2. **Optimize container configuration:**
   - Use smaller base images
   - Pre-pull images: `docker pull postgres:15`
   - Use local registry for custom images

3. **Parallel execution considerations:**
   - Avoid sharing containers across parallel tests
   - Use unique database names per test

### Test Isolation Issues

**Symptoms:**
- Tests affecting each other
- Data from one test appearing in another
- Inconsistent test results

**Solutions:**
1. **Proper cleanup between tests:**
   ```java
   @BeforeEach
   void setUp() {
       // Clean up test data
       repository.deleteAllUsers();
   }
   ```

2. **Use unique identifiers:**
   ```java
   String uniqueDbName = "testdb_" + System.currentTimeMillis();
   postgres.withDatabaseName(uniqueDbName);
   ```

3. **Transaction isolation:**
   - Use transactions for test data setup
   - Rollback transactions in test cleanup

### Memory Issues

**Symptoms:**
- OutOfMemoryError
- Tests failing due to insufficient memory

**Solutions:**
1. **Increase JVM memory:**
   ```bash
   # Java
   mvn test -Dtest.jvm.args="-Xmx2g"
   ```

2. **Optimize container memory:**
   ```java
   postgres.withCreateContainerCmdModifier(cmd -> 
       cmd.getHostConfig().withMemory(512L * 1024 * 1024)) // 512MB
   ```

3. **Monitor resource usage:**
   - Use Docker Desktop to monitor container resources
   - Check system memory usage

## Performance Issues

### Slow Container Startup

**Solutions:**
1. **Pre-pull images:**
   ```bash
   docker pull postgres:15
   docker pull redis:7
   ```

2. **Use container reuse:**
   - Share containers across test classes when possible
   - Use static containers for integration tests

3. **Optimize base images:**
   - Use Alpine variants when possible
   - Create custom images with pre-installed dependencies

### High Resource Usage

**Solutions:**
1. **Limit container resources:**
   ```java
   postgres.withCreateContainerCmdModifier(cmd -> {
       cmd.getHostConfig()
          .withMemory(256L * 1024 * 1024)  // 256MB RAM
          .withCpuCount(1L);               // 1 CPU core
   })
   ```

2. **Use resource-efficient configurations:**
   - Disable unnecessary services
   - Use minimal database configurations

## Language-Specific Issues

### Java Issues

**Common Problems:**
- Classpath issues with Testcontainers
- Maven/Gradle dependency conflicts
- JUnit 5 integration issues

**Solutions:**
```xml
<!-- Ensure correct Testcontainers version -->
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>1.19.3</version>
</dependency>
```

### Go Issues

**Common Problems:**
- Module dependency issues
- Context cancellation
- Goroutine leaks

**Solutions:**
```go
// Always use context with timeout
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Minute)
defer cancel()

// Ensure proper cleanup
defer container.Terminate(ctx)
```

### Node.js Issues

**Common Problems:**
- Async/await issues
- Promise handling
- TypeScript configuration

**Solutions:**
```typescript
// Ensure proper async handling
beforeAll(async () => {
    container = await new PostgreSqlContainer('postgres:15').start();
});

afterAll(async () => {
    await container.stop();
});
```

### Python Issues

**Common Problems:**
- Virtual environment issues
- Package dependency conflicts
- Import errors

**Solutions:**
```bash
# Use virtual environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testcontainers Cloud Issues

### Authentication Issues

**Symptoms:**
- "Invalid token" errors
- Cannot connect to Testcontainers Cloud

**Solutions:**
1. **Verify API token:**
   ```bash
   export TC_CLOUD_TOKEN=your_token_here
   echo $TC_CLOUD_TOKEN
   ```

2. **Check token permissions:**
   - Ensure token has proper scopes
   - Verify token hasn't expired

### Network Issues

**Symptoms:**
- Cannot reach Testcontainers Cloud
- SSH tunnel connection failures

**Solutions:**
1. **Check network connectivity:**
   ```bash
   curl -I https://testcontainers.cloud
   ```

2. **Firewall/proxy issues:**
   - Configure proxy settings if behind corporate firewall
   - Whitelist Testcontainers Cloud domains

### Free Tier Limitations

**Symptoms:**
- "Quota exceeded" errors
- Tests failing due to 50-minute limit
- "Single worker" environment errors

**Solutions:**
1. **Monitor usage:**
   - Check Testcontainers Cloud dashboard regularly
   - Track remaining minutes
   - Review usage patterns

2. **Optimize for free tier:**
   ```java
   // Use container reuse to minimize startup time
   @Testcontainers
   class OptimizedTest {
       @Container
       static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:13-alpine");
       
       @BeforeEach
       void setUp() {
           // Clean data, not containers
           userRepository.deleteAllUsers();
       }
   }
   ```

3. **Strategic usage:**
   - Use local Docker for development
   - Use cloud only for CI/CD or final validation
   - Batch related tests together
   - Use smaller, faster container images

### Resource Limits

**Symptoms:**
- "Resource limit exceeded" errors
- Tests failing due to quota limits

**Solutions:**
1. **Monitor usage:**
   - Check Testcontainers Cloud dashboard
   - Review usage patterns

2. **Optimize resource usage:**
   - Use smaller containers
   - Implement proper cleanup
   - Consider local testing for development
   - Focus on essential tests only in cloud

## Getting Additional Help

### Debugging Tips

1. **Enable verbose logging:**
   ```java
   // Java
   System.setProperty("testcontainers.reuse.enable", "true");
   ```

2. **Check container logs:**
   ```bash
   docker logs <container_id>
   ```

3. **Use Testcontainers Desktop:**
   - Monitor container lifecycle
   - View logs and metrics
   - Debug connection issues

### Community Resources

- [Testcontainers Slack](https://slack.testcontainers.org/)
- [GitHub Discussions](https://github.com/testcontainers/testcontainers-java/discussions)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/testcontainers)

### Lab Support

For lab-specific issues:
1. Check this troubleshooting guide
2. Review the [Common Issues](COMMON_ISSUES.md) document
3. Contact lab instructors
4. Check the lab's issue tracker
