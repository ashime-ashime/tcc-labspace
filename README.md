# Testcontainers Cloud (TCC) Lab for TSEs

A hands-on lab for Technical Support Engineers to master Testcontainers Cloud through a practical break-and-fix exercise based on real customer scenarios.

## Quick Start

```bash
# Run the enhanced interactive TSE investigation game
docker run -it ashimeashime006/tcc-lab:latest

# The mystery investigation game starts automatically!
```

**🎮 Complete Enhanced Interactive Experience:**
- **📋 Customer Analysis Phase** - Read ticket, explore supporting documents, take assessment quiz
- **🔧 Investigation Toolbox** - 10 diagnostic tools (6 essential + 4 red herrings) with command previews
- **🕵️‍♂️ Active Investigation** - Run real commands, discover clues progressively, strategic decision making
- **🎯 Solution Evaluation** - Evidence-based solution validation with detailed feedback and explanations

**No Setup Required!** TCC account, service tokens, and Testcontainers Desktop are pre-configured.

## Exercise

### The Quota Mystery (60-90 minutes)
- **Scenario**: Customer hitting TCC quota limits in GitHub Actions
- **Focus**: Billing models, usage tracking, and quota analysis
- **Skills**: Customer investigation, strategic thinking, evidence analysis, professional communication
- **Type**: Complete enhanced interactive TSE training simulation
- **Experience**: Realistic workflow from customer ticket analysis to evidence-based solution proposal
- **Features**: Real command execution, red herring tools, evidence-based solution evaluation

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

**Complete Enhanced TSE Training Simulation:**
- **Realistic customer scenarios** with complete ticket analysis
- **Strategic investigation methodology** with 10 diagnostic tools
- **Real command execution** for authentic TSE skill building
- **Evidence-based solution evaluation** with detailed feedback
- **Professional communication guidance** with response templates
- **Red herring tools** for critical thinking development
- **Progressive clue discovery** with educational insights
- **Based on actual TSE support tickets** with real diagnostic commands

**Perfect for Senior TSE skill development with complete educational depth!**