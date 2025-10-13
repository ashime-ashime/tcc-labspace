#!/usr/bin/env python3
"""
Simple PostgreSQL test that should work with TCC
Customer expects this to run in Testcontainers Cloud
"""

import pytest
from testcontainers.postgres import PostgresContainer

def test_postgres_connection():
    """Simple test to verify TCC connection"""
    # Customer expects this to run in TCC cloud environment
    with PostgresContainer("postgres:15-alpine") as postgres:
        postgres.with_env("POSTGRES_DB", "test")
        postgres.with_env("POSTGRES_USER", "test")
        postgres.with_env("POSTGRES_PASSWORD", "test")
        
        # This line fails with "No Docker activity detected"
        postgres.start()
        
        # Test database connection
        connection_string = postgres.get_connection_url()
        assert connection_string is not None
        assert "postgresql://" in connection_string
        
        print("✅ PostgreSQL test completed successfully in TCC!")

if __name__ == "__main__":
    test_postgres_connection()
