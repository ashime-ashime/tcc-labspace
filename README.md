# Testcontainers Cloud (TCC) Lab for TSEs

A hands-on lab for Technical Support Engineers to master Testcontainers Cloud through practical break-and-fix exercises based on real customer scenarios.

## Quick Start

```bash
# Run the pre-configured interactive lab
docker run -it ashimeashime006/tcc-lab:latest

# TCC is already configured - dive directly into troubleshooting!
```

**No Setup Required!** TCC account, service tokens, and Testcontainers Desktop are pre-configured.

## Exercises

### Exercise 1: The Quota Mystery (45 minutes)
- **Scenario**: Customer hitting TCC quota limits in GitHub Actions
- **Focus**: Billing models, usage tracking, and quota analysis
- **Skills**: Customer investigation and quota management

### Exercise 2: The Connection Mystery (30 minutes)  
- **Scenario**: "No Docker activity detected" errors in TCC Desktop
- **Focus**: Desktop configuration and authentication troubleshooting
- **Skills**: Configuration diagnosis and connectivity issues

### Exercise 3: The CI/CD Mystery (45 minutes)
- **Scenario**: GitHub Actions TCC authentication failures
- **Focus**: CI/CD integration and service account management
- **Skills**: Pipeline troubleshooting and automation issues

## Prerequisites

- Docker Desktop (to run the lab container)
- Basic knowledge of customer support workflows
- Experience with systematic troubleshooting approaches

## Development

```bash
# Clone and build locally
git clone https://github.com/ashime-ashime/tcc-labspace.git
cd tcc-labspace

# Build the lab
docker build -f .labspace/Dockerfile -t tcc-lab .

# Run locally
docker run -it tcc-lab
```

## Structure

```
labspace-exercises/
├── quota-mystery/       # Exercise 1: TCC billing & quota investigation
├── tcc-troubleshooting/ # Exercise 2: Desktop configuration issues
└── ci-cd-mystery/       # Exercise 3: GitHub Actions integration
```

## Learning Path

**Progressive TCC Expertise Building:**
1. **Start with billing** - Understand TCC usage and limits
2. **Build connectivity knowledge** - How TCC actually works
3. **Master integration** - TCC in CI/CD pipelines

Each exercise provides real customer pressure, pre-configured broken scenarios, systematic investigation methodology, and professional communication templates.