import psycopg2
import psycopg2.extras
from typing import List, Optional
from contextlib import contextmanager
from datetime import datetime
from user import User


class UserRepository:
    """Repository for managing User entities in the database."""

    def __init__(self, connection_string: str):
        """Initialize the repository with a database connection string."""
        self.connection_string = connection_string

    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        conn = None
        try:
            conn = psycopg2.connect(
                self.connection_string,
                cursor_factory=psycopg2.extras.RealDictCursor
            )
            yield conn
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if conn:
                conn.close()

    @contextmanager
    def get_cursor(self):
        """Context manager for database cursors."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()

    def create_user(self, user: User) -> User:
        """Creates a new user in the database."""
        query = """
            INSERT INTO users (username, email, first_name, last_name, created_at, updated_at)
            VALUES (%(username)s, %(email)s, %(first_name)s, %(last_name)s, 
                    CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            RETURNING id, created_at, updated_at
        """

        with self.get_cursor() as cursor:
            cursor.execute(query, {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            })
            
            result = cursor.fetchone()
            user.id = result['id']
            user.created_at = result['created_at']
            user.updated_at = result['updated_at']
            
            return user

    def find_by_id(self, user_id: int) -> Optional[User]:
        """Finds a user by ID."""
        query = """
            SELECT id, username, email, first_name, last_name, created_at, updated_at
            FROM users WHERE id = %s
        """

        with self.get_cursor() as cursor:
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            
            if result:
                return self._map_row_to_user(result)
            return None

    def find_by_username(self, username: str) -> Optional[User]:
        """Finds a user by username."""
        query = """
            SELECT id, username, email, first_name, last_name, created_at, updated_at
            FROM users WHERE username = %s
        """

        with self.get_cursor() as cursor:
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            
            if result:
                return self._map_row_to_user(result)
            return None

    def find_by_email(self, email: str) -> Optional[User]:
        """Finds a user by email."""
        query = """
            SELECT id, username, email, first_name, last_name, created_at, updated_at
            FROM users WHERE email = %s
        """

        with self.get_cursor() as cursor:
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            
            if result:
                return self._map_row_to_user(result)
            return None

    def update_user(self, user: User) -> User:
        """Updates an existing user."""
        query = """
            UPDATE users 
            SET username = %(username)s, email = %(email)s, first_name = %(first_name)s, 
                last_name = %(last_name)s, updated_at = CURRENT_TIMESTAMP
            WHERE id = %(id)s
            RETURNING updated_at
        """

        with self.get_cursor() as cursor:
            cursor.execute(query, {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            })
            
            result = cursor.fetchone()
            if not result:
                raise ValueError(f"User with ID {user.id} not found")
            
            user.updated_at = result['updated_at']
            return user

    def delete_user(self, user_id: int) -> bool:
        """Deletes a user by ID."""
        query = "DELETE FROM users WHERE id = %s"

        with self.get_cursor() as cursor:
            cursor.execute(query, (user_id,))
            return cursor.rowcount > 0

    def find_all_users(self) -> List[User]:
        """Retrieves all users."""
        query = """
            SELECT id, username, email, first_name, last_name, created_at, updated_at
            FROM users ORDER BY id
        """

        with self.get_cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            
            return [self._map_row_to_user(row) for row in results]

    def count_users(self) -> int:
        """Counts the total number of users."""
        query = "SELECT COUNT(*) as count FROM users"

        with self.get_cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return result['count']

    def delete_all_users(self) -> None:
        """Deletes all users (useful for test cleanup)."""
        query = "DELETE FROM users"

        with self.get_cursor() as cursor:
            cursor.execute(query)

    def execute_transaction(self, operations):
        """Executes multiple operations within a transaction."""
        with self.get_connection() as conn:
            try:
                conn.autocommit = False
                cursor = conn.cursor()
                
                result = operations(cursor)
                
                conn.commit()
                return result
            except Exception as e:
                conn.rollback()
                raise e

    def _map_row_to_user(self, row) -> User:
        """Maps a database row to a User object."""
        return User(
            id=row['id'],
            username=row['username'],
            email=row['email'],
            first_name=row['first_name'],
            last_name=row['last_name'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
        )

    def search_users(self, search_term: str) -> List[User]:
        """Searches users by username, email, first_name, or last_name."""
        query = """
            SELECT id, username, email, first_name, last_name, created_at, updated_at
            FROM users 
            WHERE username ILIKE %s OR email ILIKE %s OR first_name ILIKE %s OR last_name ILIKE %s
            ORDER BY username
        """
        
        search_pattern = f"%{search_term}%"
        
        with self.get_cursor() as cursor:
            cursor.execute(query, (search_pattern, search_pattern, search_pattern, search_pattern))
            results = cursor.fetchall()
            
            return [self._map_row_to_user(row) for row in results]

    def get_users_by_date_range(self, start_date: datetime, end_date: datetime) -> List[User]:
        """Gets users created within a date range."""
        query = """
            SELECT id, username, email, first_name, last_name, created_at, updated_at
            FROM users 
            WHERE created_at BETWEEN %s AND %s
            ORDER BY created_at
        """
        
        with self.get_cursor() as cursor:
            cursor.execute(query, (start_date, end_date))
            results = cursor.fetchall()
            
            return [self._map_row_to_user(row) for row in results]
