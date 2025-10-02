export interface User {
  id?: number;
  username: string;
  email: string;
  firstName?: string;
  lastName?: string;
  createdAt?: Date;
  updatedAt?: Date;
}

export class UserEntity implements User {
  public id?: number;
  public username: string;
  public email: string;
  public firstName?: string;
  public lastName?: string;
  public createdAt?: Date;
  public updatedAt?: Date;

  constructor(user: Partial<User> = {}) {
    this.id = user.id;
    this.username = user.username || '';
    this.email = user.email || '';
    this.firstName = user.firstName;
    this.lastName = user.lastName;
    this.createdAt = user.createdAt;
    this.updatedAt = user.updatedAt;
  }

  /**
   * Returns the full name of the user
   */
  get fullName(): string {
    if (this.firstName && this.lastName) {
      return `${this.firstName} ${this.lastName}`;
    }
    if (this.firstName) {
      return this.firstName;
    }
    if (this.lastName) {
      return this.lastName;
    }
    return '';
  }

  /**
   * Checks if the user has required fields
   */
  isValid(): boolean {
    return !!(this.username && this.email);
  }

  /**
   * Creates a new User instance with username and email
   */
  static create(username: string, email: string): UserEntity {
    return new UserEntity({ username, email });
  }

  /**
   * Creates a new User instance with all fields
   */
  static createWithNames(
    username: string,
    email: string,
    firstName: string,
    lastName: string
  ): UserEntity {
    return new UserEntity({
      username,
      email,
      firstName,
      lastName,
    });
  }

  /**
   * Updates user fields
   */
  update(updates: Partial<User>): void {
    if (updates.username !== undefined) this.username = updates.username;
    if (updates.email !== undefined) this.email = updates.email;
    if (updates.firstName !== undefined) this.firstName = updates.firstName;
    if (updates.lastName !== undefined) this.lastName = updates.lastName;
  }

  /**
   * Converts to plain object
   */
  toJSON(): User {
    return {
      id: this.id,
      username: this.username,
      email: this.email,
      firstName: this.firstName,
      lastName: this.lastName,
      createdAt: this.createdAt,
      updatedAt: this.updatedAt,
    };
  }
}
