package main

import (
	"context"
	"database/sql"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"github.com/testcontainers/testcontainers-go"
	"github.com/testcontainers/testcontainers-go/modules/postgres"
)

func TestUserRepository(t *testing.T) {
	ctx := context.Background()

	// Start PostgreSQL container
	postgresContainer, err := postgres.RunContainer(ctx,
		testcontainers.WithImage("postgres:15"),
		postgres.WithDatabase("testdb"),
		postgres.WithUsername("test"),
		postgres.WithPassword("test"),
		postgres.WithInitScripts("../../exercises/go/init.sql"),
	)
	require.NoError(t, err)
	defer postgresContainer.Terminate(ctx)

	// Get connection string
	connStr, err := postgresContainer.ConnectionString(ctx, "sslmode=disable")
	require.NoError(t, err)

	// Connect to database
	db, err := sql.Open("postgres", connStr)
	require.NoError(t, err)
	defer db.Close()

	// Create repository
	repo := NewUserRepository(db)

	// Test cleanup before each test
	cleanup := func() {
		repo.DeleteAllUsers()
	}

	t.Run("CreateUser", func(t *testing.T) {
		cleanup()

		user := NewUserWithNames("testuser", "test@example.com", "Test", "User")

		createdUser, err := repo.CreateUser(user)
		require.NoError(t, err)
		assert.NotNil(t, createdUser)
		assert.NotZero(t, createdUser.ID)
		assert.Equal(t, "testuser", createdUser.Username)
		assert.Equal(t, "test@example.com", createdUser.Email)
		assert.Equal(t, "Test", createdUser.FirstName)
		assert.Equal(t, "User", createdUser.LastName)
		assert.False(t, createdUser.CreatedAt.IsZero())
		assert.False(t, createdUser.UpdatedAt.IsZero())
	})

	t.Run("FindByID", func(t *testing.T) {
		cleanup()

		user := NewUserWithNames("finduser", "find@example.com", "Find", "User")
		createdUser, err := repo.CreateUser(user)
		require.NoError(t, err)

		foundUser, err := repo.FindByID(createdUser.ID)
		require.NoError(t, err)
		assert.NotNil(t, foundUser)
		assert.Equal(t, "finduser", foundUser.Username)
		assert.Equal(t, "find@example.com", foundUser.Email)
	})

	t.Run("FindByUsername", func(t *testing.T) {
		cleanup()

		user := NewUserWithNames("usernameuser", "username@example.com", "Username", "User")
		_, err := repo.CreateUser(user)
		require.NoError(t, err)

		foundUser, err := repo.FindByUsername("usernameuser")
		require.NoError(t, err)
		assert.NotNil(t, foundUser)
		assert.Equal(t, "username@example.com", foundUser.Email)
	})

	t.Run("FindByEmail", func(t *testing.T) {
		cleanup()

		user := NewUserWithNames("emailuser", "email@example.com", "Email", "User")
		_, err := repo.CreateUser(user)
		require.NoError(t, err)

		foundUser, err := repo.FindByEmail("email@example.com")
		require.NoError(t, err)
		assert.NotNil(t, foundUser)
		assert.Equal(t, "emailuser", foundUser.Username)
	})

	t.Run("UpdateUser", func(t *testing.T) {
		cleanup()

		user := NewUserWithNames("updateuser", "update@example.com", "Update", "User")
		createdUser, err := repo.CreateUser(user)
		require.NoError(t, err)

		originalUpdatedAt := createdUser.UpdatedAt

		// Wait a bit to ensure timestamp difference
		time.Sleep(10 * time.Millisecond)

		createdUser.FirstName = "Updated"
		createdUser.LastName = "Name"

		err = repo.UpdateUser(createdUser)
		require.NoError(t, err)

		assert.Equal(t, "Updated", createdUser.FirstName)
		assert.Equal(t, "Name", createdUser.LastName)
		assert.True(t, createdUser.UpdatedAt.After(originalUpdatedAt))
	})

	t.Run("DeleteUser", func(t *testing.T) {
		cleanup()

		user := NewUserWithNames("deleteuser", "delete@example.com", "Delete", "User")
		createdUser, err := repo.CreateUser(user)
		require.NoError(t, err)

		err = repo.DeleteUser(createdUser.ID)
		require.NoError(t, err)

		foundUser, err := repo.FindByID(createdUser.ID)
		require.NoError(t, err)
		assert.Nil(t, foundUser)
	})

	t.Run("FindAllUsers", func(t *testing.T) {
		cleanup()

		user1 := NewUserWithNames("user1", "user1@example.com", "User", "One")
		user2 := NewUserWithNames("user2", "user2@example.com", "User", "Two")

		_, err := repo.CreateUser(user1)
		require.NoError(t, err)
		_, err = repo.CreateUser(user2)
		require.NoError(t, err)

		users, err := repo.FindAllUsers()
		require.NoError(t, err)
		assert.Len(t, users, 2)

		usernames := make([]string, len(users))
		for i, user := range users {
			usernames[i] = user.Username
		}
		assert.Contains(t, usernames, "user1")
		assert.Contains(t, usernames, "user2")
	})

	t.Run("CountUsers", func(t *testing.T) {
		cleanup()

		count, err := repo.CountUsers()
		require.NoError(t, err)
		assert.Equal(t, 0, count)

		user1 := NewUserWithNames("countuser1", "count1@example.com", "Count", "User1")
		_, err = repo.CreateUser(user1)
		require.NoError(t, err)

		count, err = repo.CountUsers()
		require.NoError(t, err)
		assert.Equal(t, 1, count)

		user2 := NewUserWithNames("countuser2", "count2@example.com", "Count", "User2")
		_, err = repo.CreateUser(user2)
		require.NoError(t, err)

		count, err = repo.CountUsers()
		require.NoError(t, err)
		assert.Equal(t, 2, count)
	})

	t.Run("HandleNonExistentUser", func(t *testing.T) {
		cleanup()

		foundUser, err := repo.FindByID(999)
		require.NoError(t, err)
		assert.Nil(t, foundUser)
	})

	t.Run("PreventDuplicateUsernames", func(t *testing.T) {
		cleanup()

		user1 := NewUserWithNames("duplicate", "user1@example.com", "User", "One")
		user2 := NewUserWithNames("duplicate", "user2@example.com", "User", "Two")

		_, err := repo.CreateUser(user1)
		require.NoError(t, err)

		_, err = repo.CreateUser(user2)
		assert.Error(t, err)
		assert.Contains(t, err.Error(), "duplicate key value violates unique constraint")
	})

	t.Run("PreventDuplicateEmails", func(t *testing.T) {
		cleanup()

		user1 := NewUserWithNames("user1", "duplicate@example.com", "User", "One")
		user2 := NewUserWithNames("user2", "duplicate@example.com", "User", "Two")

		_, err := repo.CreateUser(user1)
		require.NoError(t, err)

		_, err = repo.CreateUser(user2)
		assert.Error(t, err)
		assert.Contains(t, err.Error(), "duplicate key value violates unique constraint")
	})

	t.Run("CompleteCRUDWorkflow", func(t *testing.T) {
		cleanup()

		// Create
		user := NewUserWithNames("cruduser", "crud@example.com", "CRUD", "User")
		createdUser, err := repo.CreateUser(user)
		require.NoError(t, err)
		assert.NotZero(t, createdUser.ID)

		// Read
		foundUser, err := repo.FindByID(createdUser.ID)
		require.NoError(t, err)
		assert.NotNil(t, foundUser)
		assert.Equal(t, "cruduser", foundUser.Username)

		// Update
		foundUser.FirstName = "Updated"
		err = repo.UpdateUser(foundUser)
		require.NoError(t, err)
		assert.Equal(t, "Updated", foundUser.FirstName)

		// Delete
		err = repo.DeleteUser(foundUser.ID)
		require.NoError(t, err)

		// Verify deletion
		deletedUser, err := repo.FindByID(foundUser.ID)
		require.NoError(t, err)
		assert.Nil(t, deletedUser)
	})
}
