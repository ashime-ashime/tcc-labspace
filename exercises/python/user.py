from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class User:
    """User entity representing a user in the system."""
    
    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        """Validate user data after initialization."""
        if not self.username or not self.email:
            raise ValueError("Username and email are required")

    @property
    def full_name(self) -> str:
        """Returns the full name of the user."""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.first_name:
            return self.first_name
        if self.last_name:
            return self.last_name
        return ""

    @property
    def is_valid(self) -> bool:
        """Checks if the user has required fields."""
        return bool(self.username and self.email)

    @classmethod
    def create(cls, username: str, email: str) -> "User":
        """Creates a new User instance with username and email."""
        return cls(username=username, email=email)

    @classmethod
    def create_with_names(
        cls, username: str, email: str, first_name: str, last_name: str
    ) -> "User":
        """Creates a new User instance with all fields."""
        return cls(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

    def update(self, **kwargs) -> None:
        """Updates user fields."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self) -> dict:
        """Converts to dictionary."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self) -> str:
        """String representation of the user."""
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

    def __repr__(self) -> str:
        """Detailed string representation of the user."""
        return (
            f"User(id={self.id}, username='{self.username}', email='{self.email}', "
            f"first_name='{self.first_name}', last_name='{self.last_name}', "
            f"created_at={self.created_at}, updated_at={self.updated_at})"
        )
