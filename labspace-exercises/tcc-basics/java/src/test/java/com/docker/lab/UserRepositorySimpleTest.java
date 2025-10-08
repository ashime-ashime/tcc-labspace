package com.docker.lab;

import org.junit.jupiter.api.*;
import org.testcontainers.containers.PostgreSQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Optional;

import static org.assertj.core.api.Assertions.*;

/**
 * Simple Testcontainers example for Java
 */
@Testcontainers
class UserRepositorySimpleTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");

    private static UserRepository userRepository;
    private static Connection connection;

    @BeforeAll
    static void setUp() throws SQLException {
        connection = DriverManager.getConnection(
                postgres.getJdbcUrl(),
                postgres.getUsername(),
                postgres.getPassword()
        );
        
        // Create the users table
        try (var stmt = connection.createStatement()) {
            stmt.execute("CREATE TABLE IF NOT EXISTS users (" +
                    "id SERIAL PRIMARY KEY, " +
                    "username VARCHAR(50) UNIQUE NOT NULL, " +
                    "email VARCHAR(100) UNIQUE NOT NULL, " +
                    "first_name VARCHAR(50) NOT NULL, " +
                    "last_name VARCHAR(50) NOT NULL, " +
                    "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, " +
                    "updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP" +
                    ")");
        }
        
        userRepository = new UserRepository(connection);
    }

    @AfterAll
    static void tearDown() throws SQLException {
        if (connection != null && !connection.isClosed()) {
            connection.close();
        }
    }

    @BeforeEach
    void cleanUp() throws SQLException {
        // Only clean up if the table exists and repository is initialized
        if (userRepository != null) {
            try {
                userRepository.deleteAllUsers();
            } catch (SQLException e) {
                // Ignore if table doesn't exist yet
                if (!e.getMessage().contains("does not exist")) {
                    throw e;
                }
            }
        }
    }

    @Test
    @DisplayName("Should create a user successfully")
    void shouldCreateUser() throws SQLException {
        // Given
        User user = new User.Builder()
                .username("testuser")
                .email("test@example.com")
                .firstName("Test")
                .lastName("User")
                .build();

        // When
        User createdUser = userRepository.createUser(user);

        // Then
        assertThat(createdUser).isNotNull();
        assertThat(createdUser.getId()).isNotNull();
        assertThat(createdUser.getUsername()).isEqualTo("testuser");
        assertThat(createdUser.getEmail()).isEqualTo("test@example.com");
        assertThat(createdUser.getFirstName()).isEqualTo("Test");
        assertThat(createdUser.getLastName()).isEqualTo("User");
        assertThat(createdUser.getCreatedAt()).isNotNull();

        System.out.println("✅ User created successfully: " + createdUser.getUsername());
    }

    @Test
    @DisplayName("Should find user by ID")
    void shouldFindUserById() throws SQLException {
        // Given
        User user = new User.Builder()
                .username("finduser")
                .email("find@example.com")
                .firstName("Find")
                .lastName("User")
                .build();
        User createdUser = userRepository.createUser(user);

        // When
        Optional<User> foundUser = userRepository.findById(createdUser.getId());

        // Then
        assertThat(foundUser).isPresent();
        assertThat(foundUser.get().getUsername()).isEqualTo("finduser");
        assertThat(foundUser.get().getEmail()).isEqualTo("find@example.com");

        System.out.println("✅ User found successfully: " + foundUser.get().getUsername());
    }
}
