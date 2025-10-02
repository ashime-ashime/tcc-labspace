import { Pool, PoolClient } from 'pg';
import { User, UserEntity } from './user';

export class UserRepository {
  private pool: Pool;

  constructor(pool: Pool) {
    this.pool = pool;
  }

  /**
   * Creates a new user in the database
   */
  async createUser(user: UserEntity): Promise<UserEntity> {
    const query = `
      INSERT INTO users (username, email, first_name, last_name, created_at, updated_at)
      VALUES ($1, $2, $3, $4, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
      RETURNING id, created_at, updated_at`;

    const values = [user.username, user.email, user.firstName || null, user.lastName || null];

    const client = await this.pool.connect();
    try {
      const result = await client.query(query, values);
      const row = result.rows[0];

      user.id = row.id;
      user.createdAt = row.created_at;
      user.updatedAt = row.updated_at;

      return user;
    } finally {
      client.release();
    }
  }

  /**
   * Finds a user by ID
   */
  async findById(id: number): Promise<UserEntity | null> {
    const query = `
      SELECT id, username, email, first_name, last_name, created_at, updated_at
      FROM users WHERE id = $1`;

    const client = await this.pool.connect();
    try {
      const result = await client.query(query, [id]);
      
      if (result.rows.length === 0) {
        return null;
      }

      return this.mapRowToUser(result.rows[0]);
    } finally {
      client.release();
    }
  }

  /**
   * Finds a user by username
   */
  async findByUsername(username: string): Promise<UserEntity | null> {
    const query = `
      SELECT id, username, email, first_name, last_name, created_at, updated_at
      FROM users WHERE username = $1`;

    const client = await this.pool.connect();
    try {
      const result = await client.query(query, [username]);
      
      if (result.rows.length === 0) {
        return null;
      }

      return this.mapRowToUser(result.rows[0]);
    } finally {
      client.release();
    }
  }

  /**
   * Finds a user by email
   */
  async findByEmail(email: string): Promise<UserEntity | null> {
    const query = `
      SELECT id, username, email, first_name, last_name, created_at, updated_at
      FROM users WHERE email = $1`;

    const client = await this.pool.connect();
    try {
      const result = await client.query(query, [email]);
      
      if (result.rows.length === 0) {
        return null;
      }

      return this.mapRowToUser(result.rows[0]);
    } finally {
      client.release();
    }
  }

  /**
   * Updates an existing user
   */
  async updateUser(user: UserEntity): Promise<UserEntity> {
    const query = `
      UPDATE users 
      SET username = $1, email = $2, first_name = $3, last_name = $4, updated_at = CURRENT_TIMESTAMP
      WHERE id = $5
      RETURNING updated_at`;

    const values = [
      user.username,
      user.email,
      user.firstName || null,
      user.lastName || null,
      user.id,
    ];

    const client = await this.pool.connect();
    try {
      const result = await client.query(query, values);
      
      if (result.rows.length === 0) {
        throw new Error(`User with ID ${user.id} not found`);
      }

      user.updatedAt = result.rows[0].updated_at;
      return user;
    } finally {
      client.release();
    }
  }

  /**
   * Deletes a user by ID
   */
  async deleteUser(id: number): Promise<boolean> {
    const query = 'DELETE FROM users WHERE id = $1';

    const client = await this.pool.connect();
    try {
      const result = await client.query(query, [id]);
      return result.rowCount > 0;
    } finally {
      client.release();
    }
  }

  /**
   * Retrieves all users
   */
  async findAllUsers(): Promise<UserEntity[]> {
    const query = `
      SELECT id, username, email, first_name, last_name, created_at, updated_at
      FROM users ORDER BY id`;

    const client = await this.pool.connect();
    try {
      const result = await client.query(query);
      return result.rows.map(row => this.mapRowToUser(row));
    } finally {
      client.release();
    }
  }

  /**
   * Counts the total number of users
   */
  async countUsers(): Promise<number> {
    const query = 'SELECT COUNT(*) as count FROM users';

    const client = await this.pool.connect();
    try {
      const result = await client.query(query);
      return parseInt(result.rows[0].count, 10);
    } finally {
      client.release();
    }
  }

  /**
   * Deletes all users (useful for test cleanup)
   */
  async deleteAllUsers(): Promise<void> {
    const query = 'DELETE FROM users';

    const client = await this.pool.connect();
    try {
      await client.query(query);
    } finally {
      client.release();
    }
  }

  /**
   * Executes a transaction
   */
  async executeTransaction<T>(callback: (client: PoolClient) => Promise<T>): Promise<T> {
    const client = await this.pool.connect();
    try {
      await client.query('BEGIN');
      const result = await callback(client);
      await client.query('COMMIT');
      return result;
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  }

  /**
   * Maps a database row to a UserEntity
   */
  private mapRowToUser(row: any): UserEntity {
    const user = new UserEntity();
    user.id = row.id;
    user.username = row.username;
    user.email = row.email;
    user.firstName = row.first_name;
    user.lastName = row.last_name;
    user.createdAt = row.created_at;
    user.updatedAt = row.updated_at;
    return user;
  }

  /**
   * Closes the connection pool
   */
  async close(): Promise<void> {
    await this.pool.end();
  }
}
