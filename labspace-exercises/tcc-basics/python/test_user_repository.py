import pytest
from datetime import datetime, timedelta
from testcontainers.postgres import PostgresContainer
from user import User
from user_repository import UserRepository


class TestUserRepository:
    """Test suite for UserRepository using Testcontainers."""

    @pytest.fixture(scope="class")
    def postgres_container(self):
        """Start PostgreSQL container for testing."""
        postgres = PostgresContainer("postgres:15-alpine")
        postgres.with_env("POSTGRES_DB", "test")
        postgres.with_env("POSTGRES_USER", "test")
        postgres.with_env("POSTGRES_PASSWORD", "test")
        postgres.start()
        yield postgres
        postgres.stop()

    @pytest.fixture(scope="class")
    def repository(self, postgres_container):
        """Create UserRepository instance."""
        # Connect to the test database
        connection_string = f"host={postgres_container.get_container_host_ip()} " \
                          f"port={postgres_container.get_exposed_port(5432)} " \
                          f"dbname=test user=test password=test"
        
        repo = UserRepository(connection_string)
        
        # Set up database schema
        with repo.get_connection() as conn:
            with conn.cursor() as cursor:
                # Read and execute init.sql
                with open('init.sql', 'r') as f:
                    cursor.execute(f.read())
                conn.commit()
        
        return repo

    @pytest.fixture(autouse=True)
    def cleanup(self, repository):
        """Clean up test data before each test."""
        yield
        repository.delete_all_users()

    def test_create_user(self, repository):
        """Test creating a new user."""
        user = User.create_with_names(
            "testuser", "test@example.com", "Test", "User"
        )

        created_user = repository.create_user(user)

        assert created_user.id is not None
        assert created_user.username == "testuser"
        assert created_user.email == "test@example.com"
        assert created_user.first_name == "Test"
        assert created_user.last_name == "User"
        assert created_user.created_at is not None
        assert created_user.updated_at is not None

    def test_create_user_duplicate_username(self, repository):
        """Test that duplicate usernames are prevented."""
        user1 = User.create_with_names(
            "duplicate", "user1@example.com", "User", "One"
        )
        user2 = User.create_with_names(
            "duplicate", "user2@example.com", "User", "Two"
        )

        repository.create_user(user1)

        with pytest.raises(Exception):
            repository.create_user(user2)

    def test_create_user_duplicate_email(self, repository):
        """Test that duplicate emails are prevented."""
        user1 = User.create_with_names(
            "user1", "duplicate@example.com", "User", "One"
        )
        user2 = User.create_with_names(
            "user2", "duplicate@example.com", "User", "Two"
        )

        repository.create_user(user1)

        with pytest.raises(Exception):
            repository.create_user(user2)

    def test_find_by_id(self, repository):
        """Test finding user by ID."""
        user = User.create_with_names(
            "finduser", "find@example.com", "Find", "User"
        )
        created_user = repository.create_user(user)

        found_user = repository.find_by_id(created_user.id)

        assert found_user is not None
        assert found_user.username == "finduser"
        assert found_user.email == "find@example.com"

    def test_find_by_id_not_found(self, repository):
        """Test finding non-existent user by ID."""
        found_user = repository.find_by_id(999)
        assert found_user is None

    def test_find_by_username(self, repository):
        """Test finding user by username."""
        user = User.create_with_names(
            "usernameuser", "username@example.com", "Username", "User"
        )
        repository.create_user(user)

        found_user = repository.find_by_username("usernameuser")

        assert found_user is not None
        assert found_user.email == "username@example.com"

    def test_find_by_username_not_found(self, repository):
        """Test finding non-existent user by username."""
        found_user = repository.find_by_username("nonexistent")
        assert found_user is None

    def test_find_by_email(self, repository):
        """Test finding user by email."""
        user = User.create_with_names(
            "emailuser", "email@example.com", "Email", "User"
        )
        repository.create_user(user)

        found_user = repository.find_by_email("email@example.com")

        assert found_user is not None
        assert found_user.username == "emailuser"

    def test_find_by_email_not_found(self, repository):
        """Test finding non-existent user by email."""
        found_user = repository.find_by_email("nonexistent@example.com")
        assert found_user is None

    def test_update_user(self, repository):
        """Test updating user."""
        user = User.create_with_names(
            "updateuser", "update@example.com", "Update", "User"
        )
        created_user = repository.create_user(user)
        original_updated_at = created_user.updated_at

        # Wait a bit to ensure timestamp difference
        import time
        time.sleep(0.01)

        created_user.first_name = "Updated"
        created_user.last_name = "Name"

        updated_user = repository.update_user(created_user)

        assert updated_user.first_name == "Updated"
        assert updated_user.last_name == "Name"
        assert updated_user.updated_at > original_updated_at

    def test_update_user_not_found(self, repository):
        """Test updating non-existent user."""
        user = User(id=999, username="nonexistent", email="nonexistent@example.com")

        with pytest.raises(ValueError, match="User with ID 999 not found"):
            repository.update_user(user)

    def test_delete_user(self, repository):
        """Test deleting user."""
        user = User.create_with_names(
            "deleteuser", "delete@example.com", "Delete", "User"
        )
        created_user = repository.create_user(user)

        deleted = repository.delete_user(created_user.id)

        assert deleted is True

        found_user = repository.find_by_id(created_user.id)
        assert found_user is None

    def test_delete_user_not_found(self, repository):
        """Test deleting non-existent user."""
        deleted = repository.delete_user(999)
        assert deleted is False

    def test_find_all_users(self, repository):
        """Test retrieving all users."""
        user1 = User.create_with_names(
            "user1", "user1@example.com", "User", "One"
        )
        user2 = User.create_with_names(
            "user2", "user2@example.com", "User", "Two"
        )

        repository.create_user(user1)
        repository.create_user(user2)

        users = repository.find_all_users()

        assert len(users) == 2
        usernames = [user.username for user in users]
        assert "user1" in usernames
        assert "user2" in usernames

    def test_find_all_users_empty(self, repository):
        """Test retrieving all users when none exist."""
        users = repository.find_all_users()
        assert len(users) == 0

    def test_count_users(self, repository):
        """Test counting users."""
        assert repository.count_users() == 0

        user1 = User.create_with_names(
            "countuser1", "count1@example.com", "Count", "User1"
        )
        repository.create_user(user1)
        assert repository.count_users() == 1

        user2 = User.create_with_names(
            "countuser2", "count2@example.com", "Count", "User2"
        )
        repository.create_user(user2)
        assert repository.count_users() == 2

    def test_execute_transaction_success(self, repository):
        """Test successful transaction execution."""
        def create_users(cursor):
            user1 = User.create_with_names(
                "transuser1", "trans1@example.com", "Trans", "User1"
            )
            user2 = User.create_with_names(
                "transuser2", "trans2@example.com", "Trans", "User2"
            )

            created_user1 = repository.create_user(user1)
            created_user2 = repository.create_user(user2)

            return [created_user1, created_user2]

        result = repository.execute_transaction(create_users)

        assert len(result) == 2
        assert repository.count_users() == 2

    def test_execute_transaction_rollback(self, repository):
        """Test transaction rollback on error."""
        def create_user_and_fail(cursor):
            user = User.create_with_names(
                "rollbackuser", "rollback@example.com", "Rollback", "User"
            )
            repository.create_user(user)

            # This should cause an error and rollback
            raise Exception("Transaction error")

        with pytest.raises(Exception, match="Transaction error"):
            repository.execute_transaction(create_user_and_fail)

        assert repository.count_users() == 0

    def test_search_users(self, repository):
        """Test searching users."""
        user1 = User.create_with_names(
            "john_doe", "john@example.com", "John", "Doe"
        )
        user2 = User.create_with_names(
            "jane_smith", "jane@example.com", "Jane", "Smith"
        )
        user3 = User.create_with_names(
            "bob_wilson", "bob@example.com", "Bob", "Wilson"
        )

        repository.create_user(user1)
        repository.create_user(user2)
        repository.create_user(user3)

        # Search by username
        users = repository.search_users("john")
        assert len(users) == 1
        assert users[0].username == "john_doe"

        # Search by first name
        users = repository.search_users("jane")
        assert len(users) == 1
        assert users[0].username == "jane_smith"

        # Search by last name
        users = repository.search_users("wilson")
        assert len(users) == 1
        assert users[0].username == "bob_wilson"

    def test_get_users_by_date_range(self, repository):
        """Test getting users by date range."""
        user1 = User.create_with_names(
            "olduser", "old@example.com", "Old", "User"
        )
        user2 = User.create_with_names(
            "newuser", "new@example.com", "New", "User"
        )

        created_user1 = repository.create_user(user1)
        created_user2 = repository.create_user(user2)

        # Get users created in the last minute
        start_date = datetime.now() - timedelta(minutes=1)
        end_date = datetime.now() + timedelta(minutes=1)

        users = repository.get_users_by_date_range(start_date, end_date)

        assert len(users) >= 2
        usernames = [user.username for user in users]
        assert "olduser" in usernames
        assert "newuser" in usernames

    def test_complete_crud_workflow(self, repository):
        """Test complete CRUD workflow."""
        # Create
        user = User.create_with_names(
            "cruduser", "crud@example.com", "CRUD", "User"
        )
        created_user = repository.create_user(user)
        assert created_user.id is not None

        # Read
        found_user = repository.find_by_id(created_user.id)
        assert found_user is not None
        assert found_user.username == "cruduser"

        # Update
        found_user.first_name = "Updated"
        updated_user = repository.update_user(found_user)
        assert updated_user.first_name == "Updated"

        # Delete
        deleted = repository.delete_user(updated_user.id)
        assert deleted is True

        # Verify deletion
        deleted_user = repository.find_by_id(updated_user.id)
        assert deleted_user is None

    def test_user_full_name_property(self, repository):
        """Test user full name property."""
        user = User.create_with_names(
            "fullnameuser", "fullname@example.com", "Full", "Name"
        )
        assert user.full_name == "Full Name"

        user = User.create("firstonly", "first@example.com")
        user.first_name = "First"
        assert user.full_name == "First"

        user = User.create("lastonly", "last@example.com")
        user.last_name = "Last"
        assert user.full_name == "Last"

        user = User.create("none", "none@example.com")
        assert user.full_name == ""

    def test_user_validation(self, repository):
        """Test user validation."""
        with pytest.raises(ValueError, match="Username and email are required"):
            User.create("", "test@example.com")

        with pytest.raises(ValueError, match="Username and email are required"):
            User.create("testuser", "")

        user = User.create("validuser", "valid@example.com")
        assert user.is_valid is True
