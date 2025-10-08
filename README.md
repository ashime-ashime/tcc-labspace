# Testcontainers Cloud (TCC) Lab for TSEs

A hands-on lab for Technical Support Engineers to master Testcontainers Cloud through practical exercises and real-world troubleshooting scenarios.

## 🚀 Quick Start

```bash
# Run the interactive lab
docker run -it ashimeashime006/tcc-lab:latest

# Follow the menu to choose exercises
```

## 📚 Exercises

### Exercise 1: TCC Basics (45 minutes)
- Set up Testcontainers Cloud
- Run database tests in the cloud
- Monitor free tier usage

### Exercise 2: TCC Optimization (30 minutes)  
- Implement container sharing
- Optimize free tier usage
- Learn best practices

### Exercise 3: TCC Troubleshooting (45 minutes)
- Diagnose connection issues
- Handle performance problems
- Resolve authentication issues

## 📋 Prerequisites

- Docker Desktop
- Testcontainers Desktop
- Internet connectivity for TCC
- Basic knowledge of Python or Java

## 🛠️ Development

```bash
# Clone and build locally
git clone https://github.com/ashime-ashime/tcc-labspace.git
cd tcc-labspace

# Build the lab
docker build -f .labspace/Dockerfile -t tcc-lab .

# Run locally
docker run -it tcc-lab
```

## 📁 Structure

```
labspace-exercises/
├── tcc-basics/          # Exercise 1: TCC fundamentals
├── tcc-optimization/    # Exercise 2: Free tier optimization  
└── tcc-troubleshooting/ # Exercise 3: Real TSE scenarios
```
