# 🌐 Testcontainers Cloud (TCC) Lab for TSEs - LabSpace Edition

A **professional LabSpace** designed for **Technical Support Engineers (TSEs)** to master **Testcontainers Cloud** through hands-on exercises and real-world troubleshooting scenarios.

## 🎯 Overview

This LabSpace provides a **professional learning environment** with a web-based interface for TSEs to learn Testcontainers Cloud. All testing happens in the cloud, providing a consistent and efficient learning experience.

**Primary Focus**: Testcontainers Cloud (TCC) - cloud-native containerized testing  
**Target Audience**: Technical Support Engineers (TSEs)  
**Learning Approach**: Professional LabSpace with web interface  
**Key Value**: Resource efficiency, consistency, and TCC-specific troubleshooting

## 🚀 Quick Start (LabSpace)

### For TSEs - Professional LabSpace Experience:

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd docker-testcontainers-lab

# 2. Start LabSpace (one command!)
CONTENT_PATH=$PWD docker compose -f oci://dockersamples/labspace-content-dev -f .labspace/compose.override.yaml up

# 3. Open your browser to the LabSpace interface
# 4. Start learning with TCC exercises!
```

**What this gives you:**
- ✅ **Professional web interface** - No terminal required
- ✅ **One-command setup** - Ultimate simplicity
- ✅ **Consistent environment** - Same for all TSEs
- ✅ **Live updates** - Changes visible without restart

## 🌐 LabSpace Features

### Professional Learning Environment
- **Web-based interface** - Modern, user-friendly experience
- **Interactive exercises** - Step-by-step guidance
- **Live code editing** - Make changes and see results
- **Integrated terminal** - When needed for commands

### TCC-Focused Content
- **Exercise 1**: TCC Basics - Learn cloud fundamentals
- **Exercise 2**: TCC Optimization - Maximize free tier usage
- **Exercise 3**: TCC Troubleshooting - Handle real scenarios

### Real TSE Scenarios
- **Customer tickets** - Based on actual TSE experiences
- **Troubleshooting guides** - Systematic debugging approaches
- **Best practices** - Production-ready knowledge

## 📚 Prerequisites

- **Docker Desktop** (for LabSpace)
- **Testcontainers Desktop** (for TCC connection)
- **Internet connectivity** (required for TCC)
- **Web browser** (for LabSpace interface)

## 🎓 Learning Path

### Exercise 1: TCC Basics (45 minutes)
- Set up Testcontainers Cloud
- Run first tests in cloud
- Understand TCC benefits
- Monitor free tier usage

### Exercise 2: TCC Optimization (30 minutes)
- Implement container sharing
- Optimize free tier usage
- Learn best practices
- Monitor consumption

### Exercise 3: TCC Troubleshooting (45 minutes)
- Diagnose connection issues
- Handle performance problems
- Resolve authentication issues
- Apply debugging techniques

## 🚀 Development Mode

### For Content Updates:
```bash
# Start in development mode (changes visible live)
CONTENT_PATH=$PWD docker compose -f oci://dockersamples/labspace-content-dev -f .labspace/compose.override.yaml up

# Make changes to exercises
# Changes appear automatically in LabSpace interface
```

### For Publishing:
```bash
# Push to repository
git add .
git commit -m "Update TCC exercises"
git push

# GitHub Actions automatically publishes to Docker Hub
```

## 🌟 Key Benefits

### For TSEs:
- ✅ **Professional experience** - Same as Docker's own labs
- ✅ **Web interface** - Modern, intuitive learning
- ✅ **One-command setup** - No complex configuration
- ✅ **Consistent environment** - Same for all TSEs

### For Learning:
- ✅ **TCC-focused** - All testing in cloud
- ✅ **Real scenarios** - Based on actual TSE tickets
- ✅ **Progressive learning** - Build skills step by step
- ✅ **Production-ready** - Handle real customer issues

## 📁 LabSpace Structure

```
docker-testcontainers-lab/
├── labspace.yaml                    # LabSpace configuration
├── .labspace/
│   └── compose.override.yaml        # LabSpace overrides
├── labspace-exercises/
│   ├── tcc-basics/                  # Exercise 1
│   ├── tcc-optimization/            # Exercise 2
│   └── tcc-troubleshooting/         # Exercise 3
├── exercises/                       # Original exercise files
├── .github/workflows/               # Publishing workflow
└── README-LABSPACE.md              # This file
```

## 🎯 TSE Experience

### Professional Learning Journey:
1. **Start LabSpace** - One command, web interface opens
2. **Follow exercises** - Step-by-step guidance
3. **Learn TCC** - All testing in cloud
4. **Handle scenarios** - Real TSE troubleshooting
5. **Master TCC** - Ready for customer tickets

### Key Advantages:
- **No local setup** - Just Docker + LabSpace
- **Professional interface** - Modern web experience
- **Live updates** - Changes visible immediately
- **Consistent environment** - Same for all TSEs

## 🚀 Ready to Start?

1. **Clone the repository**
2. **Run LabSpace**: `CONTENT_PATH=$PWD docker compose -f oci://dockersamples/labspace-content-dev -f .labspace/compose.override.yaml up`
3. **Open browser** to LabSpace interface
4. **Start learning** with TCC exercises!

**Welcome to professional TCC learning with LabSpace!** 🌐✨
