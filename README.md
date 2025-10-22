# Testcontainers Cloud (TCC) Support Labs

Real-world break-and-fix scenarios for Technical Support Engineers. Build your TCC troubleshooting skills through hands-on investigation of authentic customer issues.

## Quick Start

```bash
# Run the lab environment
docker run -it ashimeashime006/tcc-lab:latest

# Navigate to an exercise and start investigating
cd exercises/exercise-1-ci-timeout
cat TICKET.txt
```

**No setup required!** The environment is pre-configured and ready for investigation.

## Lab Philosophy

**Self-Directed Investigation:**
- Read actual customer tickets
- Investigate real logs and configurations
- Find issues yourself (no hand-holding)
- Senior TSE-level challenges

**Authentic TSE Experience:**
- Real support scenarios
- Customer-provided data
- Professional troubleshooting workflow
- Evidence-based problem solving

## Available Exercises

### Exercise 1: CI Pipeline Timeout

**Duration:** 20-30 minutes  
**Focus:** GitHub Actions + TCC troubleshooting

**Scenario:** Enterprise customer's CI/CD pipeline failing for 48 hours. Workflow times out during TCC setup. Local tests work perfectly. Find the root cause.

**Location:** `exercises/exercise-1-ci-timeout/`

---

*More exercises coming soon!*

## Prerequisites

- Docker Desktop
- Basic command-line skills
- TSE troubleshooting experience
- Ability to read logs and analyze configurations

## How To Use

### Starting an Exercise

```bash
# 1. Navigate to the exercise
cd exercises/exercise-1-ci-timeout

# 2. Read the customer ticket
cat TICKET.txt

# 3. Investigate customer data
ls -la customer-data/
cat customer-data/ci-logs.txt
cat customer-data/workflow/test.yml

# 4. Check investigation guide if needed
cat investigation-guide/where-to-start.md

# 5. Verify your findings
cat solution/root-cause.md
```

### Optional: TCC Diagnostic API

```bash
# Start the mock TCC API
cd /workspace/tcc-diagnostic-api
./start-api.sh

# Run diagnostic queries
curl http://localhost:8080/v1/health
curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/account
```

## Lab Structure

```
/workspace/
├── exercises/                    # All lab exercises
│   └── exercise-1-ci-timeout/   # First exercise
│       ├── TICKET.txt           # Customer support ticket
│       ├── customer-data/       # Customer-provided files
│       ├── investigation-guide/ # Optional hints
│       └── solution/            # Verification and answers
│
├── tcc-diagnostic-api/          # Optional diagnostic tool (shared)
│   ├── mock-tcc-api.py         # Mock TCC API server
│   ├── start-api.sh            # API startup script
│   └── README.md               # API documentation
│
└── .labspace/                   # Lab infrastructure
    ├── Dockerfile              # Lab environment
    └── lab-welcome.sh          # Welcome banner
```

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

## Learning Outcomes

After completing these labs, you will:

- ✅ Master systematic TCC troubleshooting methodology
- ✅ Understand GitHub Actions + TCC integration
- ✅ Diagnose account and plan-related issues
- ✅ Analyze logs and configurations effectively
- ✅ Communicate professionally with customers
- ✅ Handle real-world support scenarios confidently

## What Makes This Different

**No Hand-Holding:**
- No interactive tutorials or step-by-step guides
- Self-directed investigation like real support work
- Find clues yourself by reading files and analyzing data

**Senior TSE Level:**
- Realistic complexity
- Multiple potential issues to investigate
- Requires critical thinking and analysis
- Not obvious at first glance

**Authentic Experience:**
- Based on real customer tickets
- Actual error messages and logs
- Real TCC account scenarios
- Professional customer communication required

---

**Perfect for building Senior TSE troubleshooting skills!** 🎯
