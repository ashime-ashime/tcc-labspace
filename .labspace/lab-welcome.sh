#!/bin/bash

# Main Lab Welcome Banner (No Spoilers)
clear

cat << 'EOF'
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║            🐳 Testcontainers Cloud (TCC) Support Labs                       ║
║            Real-world break-and-fix scenarios for TSEs                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

Welcome to the TCC Support Lab environment!

This lab contains realistic customer scenarios designed to build your 
Testcontainers Cloud troubleshooting skills through hands-on investigation.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 AVAILABLE EXERCISES:

   Exercise 1: CI Pipeline Timeout
   ├─ Duration: 20-30 minutes
   ├─ Focus: GitHub Actions + TCC troubleshooting
   └─ Location: exercises/exercise-1-ci-timeout/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 QUICK START:

   # Navigate to the exercise
   cd exercises/exercise-1-ci-timeout

   # Read the customer ticket
   cat TICKET.txt

   # Start investigating the customer data
   ls -la customer-data/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 HOW THESE LABS WORK:

   1. Read the customer ticket (TICKET.txt)
   2. Investigate provided customer data
   3. Form your hypothesis based on evidence
   4. Check solution/ to verify your findings

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  IMPORTANT:

   • Investigate thoroughly - don't jump to conclusions
   • Use all available customer data
   • The answer may not be immediately obvious
   • Real TSE skills: read files, analyze logs, find patterns

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ready to investigate? The customer is waiting.

EOF

echo ""

