# Docker Testcontainers Lab

A comprehensive hands-on lab for Technical Support Engineers (TSEs) to learn and master Docker Testcontainers for integration testing.

## Overview

This lab provides practical experience with Docker Testcontainers, a powerful library that allows you to write integration tests using real services wrapped in Docker containers. TSEs will learn how to:

- Set up Testcontainers in various programming languages
- Write integration tests with real databases and services
- Use Testcontainers Cloud within free tier limitations
- Debug and troubleshoot Testcontainers issues
- Implement best practices for containerized testing

## Prerequisites

- Docker Desktop installed and running
- Basic knowledge of containerization concepts
- Familiarity with at least one programming language (Java, Go, Node.js, or Python)
- Git installed for version control

## Lab Structure

```
├── docs/                    # Lab documentation and guides
├── exercises/               # Hands-on exercises
│   ├── java/               # Java Testcontainers examples
│   ├── go/                 # Go Testcontainers examples
│   ├── nodejs/             # Node.js Testcontainers examples
│   └── python/             # Python Testcontainers examples
├── solutions/               # Exercise solutions (for instructors)
├── troubleshooting/         # Common issues and debugging guides
└── resources/              # Additional learning materials
```

## Getting Started

1. Clone this repository
2. Follow the setup instructions in [docs/SETUP.md](docs/SETUP.md)
3. Start with [docs/LAB_OVERVIEW.md](docs/LAB_OVERVIEW.md)
4. Complete exercises in order, starting with your preferred language

## Learning Path

### Beginner Level
- [Exercise 1: Basic Database Testing](exercises/basic-database-testing.md)
- [Exercise 2: Service Integration Testing](exercises/service-integration-testing.md)

### Intermediate Level
- [Exercise 3: Multi-Container Testing](exercises/multi-container-testing.md)
- [Exercise 4: Testcontainers Cloud Setup (Free Tier)](exercises/testcontainers-cloud-setup.md)

### Advanced Level
- [Exercise 5: Custom Container Development](exercises/custom-container-development.md)
- [Exercise 6: Performance Testing with Testcontainers](exercises/performance-testing.md)

## Languages Supported

- **Java**: Using Testcontainers Java library
- **Go**: Using Testcontainers Go library
- **Node.js**: Using Testcontainers Node.js library
- **Python**: Using Testcontainers Python library

## Additional Resources

- [Testcontainers Official Documentation](https://testcontainers.com/)
- [Docker Testcontainers Documentation](https://docs.docker.com/testcontainers/)
- [Testcontainers Cloud Documentation](https://testcontainers.com/cloud/docs/)
- [Troubleshooting Guide](troubleshooting/README.md)

## Support

For questions or issues during the lab:
1. Check the [Troubleshooting Guide](troubleshooting/README.md)
2. Review [Common Issues](troubleshooting/COMMON_ISSUES.md)
3. Contact the lab instructors

## License

This lab is provided for educational purposes within the organization.
