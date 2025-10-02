import { Pool } from 'pg';
import { StartedPostgreSqlContainer, PostgreSqlContainer } from '@testcontainers/postgres';
import { UserEntity, UserRepository } from '../user-repository';

describe('UserRepository', () => {
  let postgresContainer: StartedPostgreSqlContainer;
  let pool: Pool;
  let repository: UserRepository;

  beforeAll(async () => {
    // Start PostgreSQL container
    postgresContainer = await new PostgreSqlContainer('postgres:15')
      .withDatabase('testdb')
      .withUsername('test')
      .withPassword('test')
      .withInitScript('../../exercises/nodejs/init.sql')
      .start();

    // Create connection pool
    pool = new Pool({
      host: postgresContainer.getHost(),
      port: postgresContainer.getPort(),
      database: postgresContainer.getDatabase(),
      user: postgresContainer.getUsername(),
      password: postgresContainer.getPassword(),
    });

    repository = new UserRepository(pool);
  });

  afterAll(async () => {
    if (pool) {
      await pool.end();
    }
    if (postgresContainer) {
      await postgresContainer.stop();
    }
  });

  beforeEach(async () => {
    // Clean up test data before each test
    await repository.deleteAllUsers();
  });

  describe('createUser', () => {
    it('should create a new user successfully', async () => {
      const user = UserEntity.createWithNames(
        'testuser',
        'test@example.com',
        'Test',
        'User'
      );

      const createdUser = await repository.createUser(user);

      expect(createdUser).toBeDefined();
      expect(createdUser.id).toBeDefined();
      expect(createdUser.username).toBe('testuser');
      expect(createdUser.email).toBe('test@example.com');
      expect(createdUser.firstName).toBe('Test');
      expect(createdUser.lastName).toBe('User');
      expect(createdUser.createdAt).toBeDefined();
      expect(createdUser.updatedAt).toBeDefined();
    });

    it('should prevent duplicate usernames', async () => {
      const user1 = UserEntity.createWithNames(
        'duplicate',
        'user1@example.com',
        'User',
        'One'
      );
      const user2 = UserEntity.createWithNames(
        'duplicate',
        'user2@example.com',
        'User',
        'Two'
      );

      await repository.createUser(user1);

      await expect(repository.createUser(user2)).rejects.toThrow();
    });

    it('should prevent duplicate emails', async () => {
      const user1 = UserEntity.createWithNames(
        'user1',
        'duplicate@example.com',
        'User',
        'One'
      );
      const user2 = UserEntity.createWithNames(
        'user2',
        'duplicate@example.com',
        'User',
        'Two'
      );

      await repository.createUser(user1);

      await expect(repository.createUser(user2)).rejects.toThrow();
    });
  });

  describe('findById', () => {
    it('should find user by ID', async () => {
      const user = UserEntity.createWithNames(
        'finduser',
        'find@example.com',
        'Find',
        'User'
      );
      const createdUser = await repository.createUser(user);

      const foundUser = await repository.findById(createdUser.id!);

      expect(foundUser).toBeDefined();
      expect(foundUser!.username).toBe('finduser');
      expect(foundUser!.email).toBe('find@example.com');
    });

    it('should return null for non-existent user', async () => {
      const foundUser = await repository.findById(999);
      expect(foundUser).toBeNull();
    });
  });

  describe('findByUsername', () => {
    it('should find user by username', async () => {
      const user = UserEntity.createWithNames(
        'usernameuser',
        'username@example.com',
        'Username',
        'User'
      );
      await repository.createUser(user);

      const foundUser = await repository.findByUsername('usernameuser');

      expect(foundUser).toBeDefined();
      expect(foundUser!.email).toBe('username@example.com');
    });

    it('should return null for non-existent username', async () => {
      const foundUser = await repository.findByUsername('nonexistent');
      expect(foundUser).toBeNull();
    });
  });

  describe('findByEmail', () => {
    it('should find user by email', async () => {
      const user = UserEntity.createWithNames(
        'emailuser',
        'email@example.com',
        'Email',
        'User'
      );
      await repository.createUser(user);

      const foundUser = await repository.findByEmail('email@example.com');

      expect(foundUser).toBeDefined();
      expect(foundUser!.username).toBe('emailuser');
    });

    it('should return null for non-existent email', async () => {
      const foundUser = await repository.findByEmail('nonexistent@example.com');
      expect(foundUser).toBeNull();
    });
  });

  describe('updateUser', () => {
    it('should update user successfully', async () => {
      const user = UserEntity.createWithNames(
        'updateuser',
        'update@example.com',
        'Update',
        'User'
      );
      const createdUser = await repository.createUser(user);
      const originalUpdatedAt = createdUser.updatedAt;

      // Wait a bit to ensure timestamp difference
      await new Promise(resolve => setTimeout(resolve, 10));

      createdUser.firstName = 'Updated';
      createdUser.lastName = 'Name';

      const updatedUser = await repository.updateUser(createdUser);

      expect(updatedUser.firstName).toBe('Updated');
      expect(updatedUser.lastName).toBe('Name');
      expect(updatedUser.updatedAt!.getTime()).toBeGreaterThan(originalUpdatedAt!.getTime());
    });

    it('should throw error for non-existent user', async () => {
      const user = new UserEntity();
      user.id = 999;
      user.username = 'nonexistent';
      user.email = 'nonexistent@example.com';

      await expect(repository.updateUser(user)).rejects.toThrow();
    });
  });

  describe('deleteUser', () => {
    it('should delete user successfully', async () => {
      const user = UserEntity.createWithNames(
        'deleteuser',
        'delete@example.com',
        'Delete',
        'User'
      );
      const createdUser = await repository.createUser(user);

      const deleted = await repository.deleteUser(createdUser.id!);

      expect(deleted).toBe(true);

      const foundUser = await repository.findById(createdUser.id!);
      expect(foundUser).toBeNull();
    });

    it('should return false for non-existent user', async () => {
      const deleted = await repository.deleteUser(999);
      expect(deleted).toBe(false);
    });
  });

  describe('findAllUsers', () => {
    it('should return all users', async () => {
      const user1 = UserEntity.createWithNames(
        'user1',
        'user1@example.com',
        'User',
        'One'
      );
      const user2 = UserEntity.createWithNames(
        'user2',
        'user2@example.com',
        'User',
        'Two'
      );

      await repository.createUser(user1);
      await repository.createUser(user2);

      const users = await repository.findAllUsers();

      expect(users).toHaveLength(2);
      expect(users.map(u => u.username)).toEqual(
        expect.arrayContaining(['user1', 'user2'])
      );
    });

    it('should return empty array when no users exist', async () => {
      const users = await repository.findAllUsers();
      expect(users).toHaveLength(0);
    });
  });

  describe('countUsers', () => {
    it('should count users correctly', async () => {
      expect(await repository.countUsers()).toBe(0);

      const user1 = UserEntity.createWithNames(
        'countuser1',
        'count1@example.com',
        'Count',
        'User1'
      );
      await repository.createUser(user1);
      expect(await repository.countUsers()).toBe(1);

      const user2 = UserEntity.createWithNames(
        'countuser2',
        'count2@example.com',
        'Count',
        'User2'
      );
      await repository.createUser(user2);
      expect(await repository.countUsers()).toBe(2);
    });
  });

  describe('executeTransaction', () => {
    it('should execute transaction successfully', async () => {
      const result = await repository.executeTransaction(async (client) => {
        const user1 = UserEntity.createWithNames(
          'transuser1',
          'trans1@example.com',
          'Trans',
          'User1'
        );
        const user2 = UserEntity.createWithNames(
          'transuser2',
          'trans2@example.com',
          'Trans',
          'User2'
        );

        // Create users within transaction
        const createdUser1 = await repository.createUser(user1);
        const createdUser2 = await repository.createUser(user2);

        return [createdUser1, createdUser2];
      });

      expect(result).toHaveLength(2);
      expect(await repository.countUsers()).toBe(2);
    });

    it('should rollback transaction on error', async () => {
      await expect(
        repository.executeTransaction(async (client) => {
          const user1 = UserEntity.createWithNames(
            'rollbackuser1',
            'rollback1@example.com',
            'Rollback',
            'User1'
          );
          await repository.createUser(user1);

          // This should cause an error and rollback
          throw new Error('Transaction error');
        })
      ).rejects.toThrow('Transaction error');

      expect(await repository.countUsers()).toBe(0);
    });
  });

  describe('Complete CRUD workflow', () => {
    it('should handle complete CRUD operations', async () => {
      // Create
      const user = UserEntity.createWithNames(
        'cruduser',
        'crud@example.com',
        'CRUD',
        'User'
      );
      const createdUser = await repository.createUser(user);
      expect(createdUser.id).toBeDefined();

      // Read
      const foundUser = await repository.findById(createdUser.id!);
      expect(foundUser).toBeDefined();
      expect(foundUser!.username).toBe('cruduser');

      // Update
      foundUser!.firstName = 'Updated';
      const updatedUser = await repository.updateUser(foundUser!);
      expect(updatedUser.firstName).toBe('Updated');

      // Delete
      const deleted = await repository.deleteUser(updatedUser.id!);
      expect(deleted).toBe(true);

      // Verify deletion
      const deletedUser = await repository.findById(updatedUser.id!);
      expect(deletedUser).toBeNull();
    });
  });
});
