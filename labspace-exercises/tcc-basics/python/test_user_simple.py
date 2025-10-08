import pytest
from testcontainers.postgres import PostgresContainer
from user_repository import UserRepository
from user import User

def test_user_creation_simple():
    """Test user creation with local PostgreSQL container"""
    with PostgresContainer("postgres:15-alpine") as postgres:
        # Configure database
        postgres.with_env("POSTGRES_DB", "test")
        postgres.with_env("POSTGRES_USER", "test")
        postgres.with_env("POSTGRES_PASSWORD", "test")
        postgres.start()
        
        # Create connection string
        connection_string = f"host={postgres.get_container_host_ip()} " \
                          f"port={postgres.get_exposed_port(5432)} " \
                          f"dbname=test user=test password=test"
        
        # Create repository and setup schema
        repository = UserRepository(connection_string)
        with repository.get_connection() as conn:
            with conn.cursor() as cursor:
                # Create users table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(50) NOT NULL UNIQUE,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        first_name VARCHAR(50),
                        last_name VARCHAR(50),
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                conn.commit()
        
        # Test: Create a user
        user = User.create("testuser", "test@example.com")
        user.first_name = "Test"
        user.last_name = "User"
        
        created_user = repository.create_user(user)
        
        # Assertions
        assert created_user.id is not None
        assert created_user.username == "testuser"
        assert created_user.email == "test@example.com"
        assert created_user.first_name == "Test"
        assert created_user.full_name == "Test User"
        
        print(f"✅ User created successfully: {created_user.username}")

def test_user_retrieval_simple():
    """Test user retrieval with local PostgreSQL container"""
    with PostgresContainer("postgres:15-alpine") as postgres:
        # Setup (same as above)
        postgres.with_env("POSTGRES_DB", "test")
        postgres.with_env("POSTGRES_USER", "test")
        postgres.with_env("POSTGRES_PASSWORD", "test")
        postgres.start()
        
        connection_string = f"host={postgres.get_container_host_ip()} " \
                          f"port={postgres.get_exposed_port(5432)} " \
                          f"dbname=test user=test password=test"
        
        repository = UserRepository(connection_string)
        with repository.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        username VARCHAR(50) NOT NULL UNIQUE,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        first_name VARCHAR(50),
                        last_name VARCHAR(50),
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                conn.commit()
        
        # Test: Create and retrieve user
        user = User.create("retrievaluser", "retrieval@example.com")
        created_user = repository.create_user(user)
        
        # Retrieve user by ID
        found_user = repository.find_by_id(created_user.id)
        
        # Assertions
        assert found_user is not None
        assert found_user.username == "retrievaluser"
        assert found_user.email == "retrieval@example.com"
        
        print(f"✅ User retrieved successfully: {found_user.username}")
