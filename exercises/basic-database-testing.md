# Exercise 1: Basic Database Testing with Testcontainers

## Learning Objectives

By the end of this exercise, you will be able to:
- Set up a Testcontainers-based test with a real database
- Write integration tests that interact with PostgreSQL
- Understand container lifecycle management
- Implement proper test cleanup and isolation

## Prerequisites

- Docker Desktop running
- Testcontainers Desktop installed and connected
- Programming language environment set up
- Basic understanding of SQL and databases

## Exercise Overview

In this exercise, you'll create a simple application that manages users and write integration tests using Testcontainers to test against a real PostgreSQL database.

## Part 1: Setting Up the Test Environment

### Step 1: Create Project Structure

Navigate to your chosen language directory and set up the basic project structure:

```bash
# Choose your language directory
cd exercises/java    # or go, nodejs, python
```

### Step 2: Add Dependencies

Add the necessary Testcontainers dependencies for your language:

#### Java (Maven)
Add to `pom.xml`:
```xml
<dependencies>
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>1.19.3</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>postgresql</artifactId>
        <version>1.19.3</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <version>42.6.0</version>
    </dependency>
</dependencies>
```

#### Go
```bash
go get github.com/testcontainers/testcontainers-go
go get github.com/testcontainers/testcontainers-go/modules/postgres
go get github.com/lib/pq
```

#### Node.js
```bash
npm install --save-dev @testcontainers/node
npm install --save-dev @testcontainers/postgres
npm install pg
```

#### Python
```bash
pip install testcontainers[postgres]
pip install psycopg2-binary
```

## Part 2: Create the User Management Application

### Step 1: Define the User Model

Create a simple User model/struct/class:

#### Java
```java
public class User {
    private Long id;
    private String username;
    private String email;
    
    // Constructors, getters, setters
}
```

#### Go
```go
type User struct {
    ID       int    `json:"id"`
    Username string `json:"username"`
    Email    string `json:"email"`
}
```

#### Node.js (TypeScript)
```typescript
interface User {
    id?: number;
    username: string;
    email: string;
}
```

#### Python
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int] = None
    username: str = ""
    email: str = ""
```

### Step 2: Create Database Schema

Create a SQL script to set up the users table:

```sql
-- init.sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Part 3: Implement Database Operations

Create a UserRepository class/module that handles database operations:

### Core Methods to Implement:
1. `createUser(user)` - Insert a new user
2. `findUserById(id)` - Find user by ID
3. `findUserByUsername(username)` - Find user by username
4. `updateUser(user)` - Update user information
5. `deleteUser(id)` - Delete user by ID
6. `listAllUsers()` - Get all users

## Part 4: Write Testcontainers Tests

### Step 1: Set Up Test Class

Create a test class that uses Testcontainers to spin up a PostgreSQL container:

#### Java
```java
@Testcontainers
class UserRepositoryTest {
    
    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test")
            .withInitScript("init.sql");
    
    @Test
    void shouldCreateUser() {
        // Test implementation
    }
}
```

#### Go
```go
func TestUserRepository(t *testing.T) {
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
    
    // Test implementation
}
```

#### Node.js
```typescript
describe('UserRepository', () => {
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
    
    test('should create user', async () => {
        // Test implementation
    });
});
```

#### Python
```python
import pytest
from testcontainers.postgres import PostgresContainer

class TestUserRepository:
    
    @pytest.fixture(scope="class")
    def postgres_container(self):
        with PostgresContainer("postgres:15") as postgres:
            postgres.with_database("testdb")
            postgres.with_username("test")
            postgres.with_password("test")
            postgres.with_init_script("init.sql")
            yield postgres
    
    def test_create_user(self, postgres_container):
        # Test implementation
```

### Step 2: Implement Test Cases

Write comprehensive tests for all repository methods:

1. **Test User Creation**
   - Create a user with valid data
   - Verify the user is stored correctly
   - Test with duplicate username/email (should fail)

2. **Test User Retrieval**
   - Find user by ID
   - Find user by username
   - Handle non-existent user scenarios

3. **Test User Updates**
   - Update user information
   - Verify changes are persisted
   - Test updating non-existent user

4. **Test User Deletion**
   - Delete existing user
   - Verify user is removed
   - Test deleting non-existent user

5. **Test User Listing**
   - List all users
   - Test with empty database
   - Test with multiple users

### Step 3: Add Integration Tests

Create tests that verify the complete user management workflow:

1. **Complete CRUD Workflow**
   - Create, read, update, delete a user in sequence
   - Verify data consistency throughout

2. **Transaction Testing**
   - Test rollback scenarios
   - Test commit scenarios

## Part 5: Advanced Testing Scenarios

### Step 1: Test Data Setup and Cleanup

Implement proper test data management:

```java
// Java example
@BeforeEach
void setUp() {
    // Clean up any existing test data
    repository.deleteAllUsers();
}

@AfterEach
void tearDown() {
    // Clean up test data
    repository.deleteAllUsers();
}
```

### Step 2: Test with Different Database Configurations

Test your application with different PostgreSQL versions:

```java
@Container
static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:13")
    .withDatabaseName("testdb")
    .withUsername("test")
    .withPassword("test");
```

### Step 3: Performance Testing

Add tests that verify performance characteristics:

```java
@Test
void shouldHandleLargeNumberOfUsers() {
    // Create 1000 users and verify performance
    List<User> users = createManyUsers(1000);
    
    long startTime = System.currentTimeMillis();
    repository.createUsers(users);
    long endTime = System.currentTimeMillis();
    
    assertThat(endTime - startTime).isLessThan(5000); // 5 seconds
}
```

## Part 6: Verification and Testing

### Step 1: Run Your Tests

Execute your tests and verify they pass:

```bash
# Java
mvn test

# Go
go test -v

# Node.js
npm test

# Python
pytest -v
```

### Step 2: Verify Container Behavior

1. Check that containers start and stop properly
2. Verify database connections are established
3. Confirm test isolation (no data leakage between tests)

### Step 3: Check Testcontainers Desktop

1. Open Testcontainers Desktop
2. Verify that containers are being created and destroyed
3. Check resource usage and performance metrics

## Exercise Checklist

Complete the following tasks:

- [ ] Set up project with Testcontainers dependencies
- [ ] Create User model and database schema
- [ ] Implement UserRepository with all CRUD operations
- [ ] Write comprehensive test suite using Testcontainers
- [ ] Test all repository methods (create, read, update, delete, list)
- [ ] Implement proper test data setup and cleanup
- [ ] Add integration tests for complete workflows
- [ ] Verify tests run successfully and containers are managed properly
- [ ] Test with different database configurations
- [ ] Add performance tests for large datasets

## Troubleshooting

### Common Issues:

1. **Container startup failures**
   - Check Docker Desktop is running
   - Verify port availability
   - Check container image availability

2. **Database connection issues**
   - Verify connection parameters
   - Check database initialization scripts
   - Ensure proper wait strategies

3. **Test isolation problems**
   - Implement proper cleanup between tests
   - Use unique database names per test
   - Verify transaction handling

## Next Steps

After completing this exercise:
1. Review your test coverage and identify any gaps
2. Experiment with different database configurations
3. Try running tests in parallel
4. Move on to [Exercise 2: Service Integration Testing](service-integration-testing.md)

## Learning Reflection

Consider these questions:
1. How does testing with a real database differ from mocking?
2. What are the benefits of using Testcontainers over embedded databases?
3. How can you ensure test reliability and repeatability?
4. What strategies can you use to optimize test performance?
