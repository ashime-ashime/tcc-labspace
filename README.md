# Testcontainers Cloud (TCC) Lab for TSEs

A hands-on lab for Technical Support Engineers to master Testcontainers Cloud through a practical break-and-fix exercise based on real customer scenarios.

## Quick Start

```bash
# Run the enhanced interactive TSE investigation game
docker run -it ashimeashime006/tcc-lab:latest

# The mystery investigation game starts automatically!
```

**🎮 Enhanced Interactive Experience:**
- **📋 Customer Analysis Phase** - Read ticket, take assessment quiz, form hypothesis
- **🔧 Investigation Toolbox** - See commands + expected outputs + analysis tips
- **🕵️‍♂️ Active Investigation** - Run diagnostic tools with confidence
- **🎯 Solution Proposal** - Apply findings, draft customer response

**No Setup Required!** TCC account, service tokens, and Testcontainers Desktop are pre-configured.

## Exercise

### The Quota Mystery (45-60 minutes)
- **Scenario**: Customer hitting TCC quota limits in GitHub Actions
- **Focus**: Billing models, usage tracking, and quota analysis
- **Skills**: Customer investigation and quota management
- **Type**: Enhanced interactive TSE training simulation
- **Experience**: Complete investigation workflow from ticket analysis to solution proposal

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
└── quota-mystery/       # The Quota Mystery: TCC billing & quota investigation
    ├── customer-report/ # Real customer data and broken configurations
    ├── solutions/       # Working solutions and response templates
    └── tse-investigation/ # Systematic investigation methodology
```

## Learning Approach

**Real TSE Experience:**
- Pre-configured broken scenario ready to investigate
- Systematic investigation methodology
- Professional customer communication templates
- Complete working solutions
- Based on actual TSE support tickets