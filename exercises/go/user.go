package main

import (
	"time"
)

// User represents a user in the system
type User struct {
	ID        int       `json:"id" db:"id"`
	Username  string    `json:"username" db:"username"`
	Email     string    `json:"email" db:"email"`
	FirstName string    `json:"first_name" db:"first_name"`
	LastName  string    `json:"last_name" db:"last_name"`
	CreatedAt time.Time `json:"created_at" db:"created_at"`
	UpdatedAt time.Time `json:"updated_at" db:"updated_at"`
}

// NewUser creates a new User instance with the provided username and email
func NewUser(username, email string) *User {
	return &User{
		Username: username,
		Email:    email,
	}
}

// NewUserWithNames creates a new User instance with all fields
func NewUserWithNames(username, email, firstName, lastName string) *User {
	return &User{
		Username:  username,
		Email:     email,
		FirstName: firstName,
		LastName:  lastName,
	}
}

// FullName returns the full name of the user
func (u *User) FullName() string {
	if u.FirstName != "" && u.LastName != "" {
		return u.FirstName + " " + u.LastName
	}
	if u.FirstName != "" {
		return u.FirstName
	}
	if u.LastName != "" {
		return u.LastName
	}
	return ""
}

// IsValid checks if the user has required fields
func (u *User) IsValid() bool {
	return u.Username != "" && u.Email != ""
}
