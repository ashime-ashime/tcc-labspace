# Common Issues and Solutions

This document provides quick solutions to the most frequently encountered issues in the Docker Testcontainers lab.

## Quick Fixes

### Issue: "Docker daemon not running"
**Solution:** Start Docker Desktop and wait for it to fully initialize.

### Issue: "Port already in use"
**Solution:** 
```bash
# Find and kill the process using the port
lsof -i :5432
kill -9 <PID>
```

### Issue: "Container startup timeout"
**Solution:** Increase timeout in your test configuration:
```java
postgres.withStartupTimeout(Duration.ofMinutes(5))
```

### Issue: "Permission denied" (Linux/macOS)
**Solution:**
```bash
sudo usermod -aG docker $USER
# Log out and back in
```

### Issue: Tests are slow
**Solution:** 
1. Pre-pull images: `docker pull postgres:15`
2. Use container reuse across test classes
3. Close unnecessary applications

### Issue: "Quota exceeded" in Testcontainers Cloud
**Solution:** 
1. Check remaining minutes in dashboard
2. Use local Docker for development
3. Optimize container reuse and test batching

## Detailed Solutions

### Database Connection Issues

| Error | Cause | Solution |
|-------|-------|----------|
| `Connection refused` | Container not ready | Add wait strategy |
| `Authentication failed` | Wrong credentials | Check username/password |
| `Database does not exist` | Wrong database name | Verify database configuration |
| `Table does not exist` | Init script not running | Check script path and syntax |

### Container Management Issues

| Error | Cause | Solution |
|-------|-------|----------|
| `Container not found` | Container cleanup issue | Use `@Testcontainers` annotation |
| `Out of memory` | Insufficient resources | Increase JVM memory or container limits |
| `Image pull failed` | Network/registry issue | Check internet connection, try different registry |

### Test Execution Issues

| Error | Cause | Solution |
|-------|-------|----------|
| `Test timeout` | Slow container startup | Increase timeout or optimize container |
| `Data not found` | Test isolation issue | Add proper cleanup in `@BeforeEach` |
| `Inconsistent results` | Race conditions | Use proper synchronization |

### Testcontainers Cloud Issues

| Error | Cause | Solution |
|-------|-------|----------|
| `Quota exceeded` | Used all 50 free minutes | Use local Docker for development |
| `Single worker limit` | Trying to run parallel tests | Run tests sequentially |
| `Authentication failed` | Invalid or expired token | Check API token validity |

## Platform-Specific Issues

### Windows
- **WSL2 issues:** Ensure WSL2 is properly configured
- **Path issues:** Use forward slashes in file paths
- **Performance:** Allocate more resources to Docker Desktop

### macOS
- **File permissions:** Check Docker Desktop file sharing settings
- **Resource limits:** Increase Docker Desktop memory allocation
- **Network issues:** Reset Docker Desktop network settings

### Linux
- **User groups:** Add user to docker group
- **Systemd issues:** Ensure Docker service is running
- **SELinux:** Configure SELinux policies if needed

## Performance Optimization

### Container Startup Optimization
1. Use Alpine-based images
2. Pre-pull commonly used images
3. Implement container reuse
4. Optimize initialization scripts

### Memory Optimization
1. Limit container memory usage
2. Use smaller base images
3. Implement proper cleanup
4. Monitor resource usage

### Network Optimization
1. Use local registries for custom images
2. Optimize network configurations
3. Use container networking features
4. Minimize external dependencies

## Debugging Checklist

Before seeking help, check:

- [ ] Docker Desktop is running
- [ ] Sufficient system resources available
- [ ] Network connectivity is working
- [ ] All dependencies are installed correctly
- [ ] Testcontainers version is compatible
- [ ] Container images are accessible
- [ ] Port conflicts are resolved
- [ ] File permissions are correct
- [ ] Environment variables are set
- [ ] Logs don't show obvious errors

## Emergency Recovery

If your environment is completely broken:

1. **Reset Docker Desktop:**
   - Stop Docker Desktop
   - Reset to factory defaults
   - Restart and reconfigure

2. **Clean up containers:**
   ```bash
   docker system prune -a
   docker volume prune
   ```

3. **Reinstall dependencies:**
   ```bash
   # For Node.js
   rm -rf node_modules package-lock.json
   npm install
   
   # For Python
   rm -rf venv
   python -m venv venv
   pip install -r requirements.txt
   ```

4. **Start fresh:**
   - Clone the lab repository again
   - Follow setup instructions from scratch
   - Run a simple test to verify everything works
