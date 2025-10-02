package main

import (
	"database/sql"
	"fmt"
	"time"

	_ "github.com/lib/pq"
)

// UserRepository handles database operations for User entities
type UserRepository struct {
	db *sql.DB
}

// NewUserRepository creates a new UserRepository instance
func NewUserRepository(db *sql.DB) *UserRepository {
	return &UserRepository{db: db}
}

// CreateUser creates a new user in the database
func (r *UserRepository) CreateUser(user *User) (*User, error) {
	query := `
		INSERT INTO users (username, email, first_name, last_name, created_at, updated_at)
		VALUES ($1, $2, $3, $4, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
		RETURNING id, created_at, updated_at`

	var id int
	var createdAt, updatedAt time.Time

	err := r.db.QueryRow(query, user.Username, user.Email, user.FirstName, user.LastName).
		Scan(&id, &createdAt, &updatedAt)
	if err != nil {
		return nil, fmt.Errorf("failed to create user: %w", err)
	}

	user.ID = id
	user.CreatedAt = createdAt
	user.UpdatedAt = updatedAt

	return user, nil
}

// FindByID finds a user by ID
func (r *UserRepository) FindByID(id int) (*User, error) {
	query := `
		SELECT id, username, email, first_name, last_name, created_at, updated_at
		FROM users WHERE id = $1`

	user := &User{}
	err := r.db.QueryRow(query, id).Scan(
		&user.ID, &user.Username, &user.Email, &user.FirstName, &user.LastName,
		&user.CreatedAt, &user.UpdatedAt,
	)

	if err != nil {
		if err == sql.ErrNoRows {
			return nil, nil // User not found
		}
		return nil, fmt.Errorf("failed to find user by ID: %w", err)
	}

	return user, nil
}

// FindByUsername finds a user by username
func (r *UserRepository) FindByUsername(username string) (*User, error) {
	query := `
		SELECT id, username, email, first_name, last_name, created_at, updated_at
		FROM users WHERE username = $1`

	user := &User{}
	err := r.db.QueryRow(query, username).Scan(
		&user.ID, &user.Username, &user.Email, &user.FirstName, &user.LastName,
		&user.CreatedAt, &user.UpdatedAt,
	)

	if err != nil {
		if err == sql.ErrNoRows {
			return nil, nil // User not found
		}
		return nil, fmt.Errorf("failed to find user by username: %w", err)
	}

	return user, nil
}

// FindByEmail finds a user by email
func (r *UserRepository) FindByEmail(email string) (*User, error) {
	query := `
		SELECT id, username, email, first_name, last_name, created_at, updated_at
		FROM users WHERE email = $1`

	user := &User{}
	err := r.db.QueryRow(query, email).Scan(
		&user.ID, &user.Username, &user.Email, &user.FirstName, &user.LastName,
		&user.CreatedAt, &user.UpdatedAt,
	)

	if err != nil {
		if err == sql.ErrNoRows {
			return nil, nil // User not found
		}
		return nil, fmt.Errorf("failed to find user by email: %w", err)
	}

	return user, nil
}

// UpdateUser updates an existing user
func (r *UserRepository) UpdateUser(user *User) error {
	query := `
		UPDATE users 
		SET username = $1, email = $2, first_name = $3, last_name = $4, updated_at = CURRENT_TIMESTAMP
		WHERE id = $5`

	result, err := r.db.Exec(query, user.Username, user.Email, user.FirstName, user.LastName, user.ID)
	if err != nil {
		return fmt.Errorf("failed to update user: %w", err)
	}

	rowsAffected, err := result.RowsAffected()
	if err != nil {
		return fmt.Errorf("failed to get rows affected: %w", err)
	}

	if rowsAffected == 0 {
		return fmt.Errorf("user with ID %d not found", user.ID)
	}

	// Update the UpdatedAt timestamp
	err = r.db.QueryRow("SELECT updated_at FROM users WHERE id = $1", user.ID).Scan(&user.UpdatedAt)
	if err != nil {
		return fmt.Errorf("failed to get updated timestamp: %w", err)
	}

	return nil
}

// DeleteUser deletes a user by ID
func (r *UserRepository) DeleteUser(id int) error {
	query := "DELETE FROM users WHERE id = $1"

	result, err := r.db.Exec(query, id)
	if err != nil {
		return fmt.Errorf("failed to delete user: %w", err)
	}

	rowsAffected, err := result.RowsAffected()
	if err != nil {
		return fmt.Errorf("failed to get rows affected: %w", err)
	}

	if rowsAffected == 0 {
		return fmt.Errorf("user with ID %d not found", id)
	}

	return nil
}

// FindAllUsers retrieves all users
func (r *UserRepository) FindAllUsers() ([]*User, error) {
	query := `
		SELECT id, username, email, first_name, last_name, created_at, updated_at
		FROM users ORDER BY id`

	rows, err := r.db.Query(query)
	if err != nil {
		return nil, fmt.Errorf("failed to query users: %w", err)
	}
	defer rows.Close()

	var users []*User
	for rows.Next() {
		user := &User{}
		err := rows.Scan(
			&user.ID, &user.Username, &user.Email, &user.FirstName, &user.LastName,
			&user.CreatedAt, &user.UpdatedAt,
		)
		if err != nil {
			return nil, fmt.Errorf("failed to scan user: %w", err)
		}
		users = append(users, user)
	}

	if err = rows.Err(); err != nil {
		return nil, fmt.Errorf("error iterating over rows: %w", err)
	}

	return users, nil
}

// CountUsers returns the total number of users
func (r *UserRepository) CountUsers() (int, error) {
	query := "SELECT COUNT(*) FROM users"

	var count int
	err := r.db.QueryRow(query).Scan(&count)
	if err != nil {
		return 0, fmt.Errorf("failed to count users: %w", err)
	}

	return count, nil
}

// DeleteAllUsers deletes all users (useful for test cleanup)
func (r *UserRepository) DeleteAllUsers() error {
	query := "DELETE FROM users"

	_, err := r.db.Exec(query)
	if err != nil {
		return fmt.Errorf("failed to delete all users: %w", err)
	}

	return nil
}

// Close closes the database connection
func (r *UserRepository) Close() error {
	if r.db != nil {
		return r.db.Close()
	}
	return nil
}
