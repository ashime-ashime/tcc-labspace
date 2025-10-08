import pytest
from testcontainers.postgres import PostgresContainer
import psycopg2

def test_postgres_connection():
    """Simple test to verify TCC connection"""
    with PostgresContainer("postgres:15-alpine") as postgres:
        postgres.with_env("POSTGRES_DB", "test")
        postgres.with_env("POSTGRES_USER", "test")
        postgres.with_env("POSTGRES_PASSWORD", "test")
        postgres.start()
        
        # Test database connection
        conn = psycopg2.connect(
            host=postgres.get_container_host_ip(),
            port=postgres.get_exposed_port(5432),
            database="test",
            user="test",
            password="test"
        )
        
        # Create a simple table and insert data
        with conn.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(50))")
            cursor.execute("INSERT INTO users (name) VALUES (%s)", ("Test User",))
            conn.commit()
            
            # Verify the data
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchone()
            assert result[1] == "Test User"
        
        conn.close()
        print("✅ PostgreSQL test completed successfully in TCC!")

if __name__ == "__main__":
    test_postgres_connection()
