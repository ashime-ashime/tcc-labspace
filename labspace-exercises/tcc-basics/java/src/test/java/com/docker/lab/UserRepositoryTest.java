package com.docker.lab;

import org.junit.jupiter.api.*;
import org.testcontainers.containers.PostgreSQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.*;

/**
 * Integration tests for UserRepository using Testcontainers.
 * These tests demonstrate how to test database operations with real PostgreSQL containers.
 */
@Testcontainers
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
class UserRepositoryTest {

    @Container
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test")
            .withInitScript("init.sql");

    private static UserRepository userRepository;
    private static Connection connection;

    @BeforeAll
    static void setUp() throws SQLException {
        // Get connection from the container
        connection = DriverManager.getConnection(
                postgres.getJdbcUrl(),
                postgres.getUsername(),
                postgres.getPassword()
        );
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
        // Clean up test data before each test
        userRepository.deleteAllUsers();
    }

    @Test
    @Order(1)
    @DisplayName("Should create a new user successfully")
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
        assertThat(createdUser.getUpdatedAt()).isNotNull();
    }

    @Test
    @Order(2)
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
    }

    @Test
    @Order(3)
    @DisplayName("Should find user by username")
    void shouldFindUserByUsername() throws SQLException {
        // Given
        User user = new User.Builder()
                .username("usernameuser")
                .email("username@example.com")
                .firstName("Username")
                .lastName("User")
                .build();
        userRepository.createUser(user);

        // When
        Optional<User> foundUser = userRepository.findByUsername("usernameuser");

        // Then
        assertThat(foundUser).isPresent();
        assertThat(foundUser.get().getEmail()).isEqualTo("username@example.com");
    }

    @Test
    @Order(4)
    @DisplayName("Should find user by email")
    void shouldFindUserByEmail() throws SQLException {
        // Given
        User user = new User.Builder()
                .username("emailuser")
                .email("email@example.com")
                .firstName("Email")
                .lastName("User")
                .build();
        userRepository.createUser(user);

        // When
        Optional<User> foundUser = userRepository.findByEmail("email@example.com");

        // Then
        assertThat(foundUser).isPresent();
        assertThat(foundUser.get().getUsername()).isEqualTo("emailuser");
    }

    @Test
    @Order(5)
    @DisplayName("Should update user successfully")
    void shouldUpdateUser() throws SQLException {
        // Given
        User user = new User.Builder()
                .username("updateuser")
                .email("update@example.com")
                .firstName("Update")
                .lastName("User")
                .build();
        User createdUser = userRepository.createUser(user);

        // When
        createdUser.setFirstName("Updated");
        createdUser.setLastName("Name");
        User updatedUser = userRepository.updateUser(createdUser);

        // Then
        assertThat(updatedUser.getFirstName()).isEqualTo("Updated");
        assertThat(updatedUser.getLastName()).isEqualTo("Name");
        assertThat(updatedUser.getUpdatedAt()).isAfter(updatedUser.getCreatedAt());
    }

    @Test
    @Order(6)
    @DisplayName("Should delete user successfully")
    void shouldDeleteUser() throws SQLException {
        // Given
        User user = new User.Builder()
                .username("deleteuser")
                .email("delete@example.com")
                .firstName("Delete")
                .lastName("User")
                .build();
        User createdUser = userRepository.createUser(user);
        Long userId = createdUser.getId();

        // When
        boolean deleted = userRepository.deleteUser(userId);

        // Then
        assertThat(deleted).isTrue();
        Optional<User> foundUser = userRepository.findById(userId);
        assertThat(foundUser).isEmpty();
    }

    @Test
    @Order(7)
    @DisplayName("Should find all users")
    void shouldFindAllUsers() throws SQLException {
        // Given
        User user1 = new User.Builder()
                .username("user1")
                .email("user1@example.com")
                .firstName("User")
                .lastName("One")
                .build();
        User user2 = new User.Builder()
                .username("user2")
                .email("user2@example.com")
                .firstName("User")
                .lastName("Two")
                .build();

        userRepository.createUser(user1);
        userRepository.createUser(user2);

        // When
        List<User> users = userRepository.findAllUsers();

        // Then
        assertThat(users).hasSize(2);
        assertThat(users).extracting(User::getUsername)
                .containsExactlyInAnyOrder("user1", "user2");
    }

    @Test
    @Order(8)
    @DisplayName("Should count users correctly")
    void shouldCountUsers() throws SQLException {
        // Given
        assertThat(userRepository.countUsers()).isZero();

        User user1 = new User.Builder()
                .username("countuser1")
                .email("count1@example.com")
                .firstName("Count")
                .lastName("User1")
                .build();
        User user2 = new User.Builder()
                .username("countuser2")
                .email("count2@example.com")
                .firstName("Count")
                .lastName("User2")
                .build();

        userRepository.createUser(user1);
        assertThat(userRepository.countUsers()).isOne();

        userRepository.createUser(user2);
        assertThat(userRepository.countUsers()).isEqualTo(2);
    }

    @Test
    @Order(9)
    @DisplayName("Should handle non-existent user gracefully")
    void shouldHandleNonExistentUser() throws SQLException {
        // When
        Optional<User> foundUser = userRepository.findById(999L);

        // Then
        assertThat(foundUser).isEmpty();
    }

    @Test
    @Order(10)
    @DisplayName("Should prevent duplicate usernames")
    void shouldPreventDuplicateUsernames() throws SQLException {
        // Given
        User user1 = new User.Builder()
                .username("duplicate")
                .email("user1@example.com")
                .firstName("User")
                .lastName("One")
                .build();
        User user2 = new User.Builder()
                .username("duplicate")
                .email("user2@example.com")
                .firstName("User")
                .lastName("Two")
                .build();

        userRepository.createUser(user1);

        // When & Then
        assertThatThrownBy(() -> userRepository.createUser(user2))
                .isInstanceOf(SQLException.class);
    }

    @Test
    @Order(11)
    @DisplayName("Should prevent duplicate emails")
    void shouldPreventDuplicateEmails() throws SQLException {
        // Given
        User user1 = new User.Builder()
                .username("user1")
                .email("duplicate@example.com")
                .firstName("User")
                .lastName("One")
                .build();
        User user2 = new User.Builder()
                .username("user2")
                .email("duplicate@example.com")
                .firstName("User")
                .lastName("Two")
                .build();

        userRepository.createUser(user1);

        // When & Then
        assertThatThrownBy(() -> userRepository.createUser(user2))
                .isInstanceOf(SQLException.class);
    }

    @Test
    @Order(12)
    @DisplayName("Should handle complete CRUD workflow")
    void shouldHandleCompleteCrudWorkflow() throws SQLException {
        // Create
        User user = new User.Builder()
                .username("cruduser")
                .email("crud@example.com")
                .firstName("CRUD")
                .lastName("User")
                .build();
        User createdUser = userRepository.createUser(user);
        assertThat(createdUser.getId()).isNotNull();

        // Read
        Optional<User> foundUser = userRepository.findById(createdUser.getId());
        assertThat(foundUser).isPresent();
        assertThat(foundUser.get().getUsername()).isEqualTo("cruduser");

        // Update
        foundUser.get().setFirstName("Updated");
        User updatedUser = userRepository.updateUser(foundUser.get());
        assertThat(updatedUser.getFirstName()).isEqualTo("Updated");

        // Delete
        boolean deleted = userRepository.deleteUser(updatedUser.getId());
        assertThat(deleted).isTrue();

        // Verify deletion
        Optional<User> deletedUser = userRepository.findById(updatedUser.getId());
        assertThat(deletedUser).isEmpty();
    }
}
