#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                    🔍 TSE ANALYSIS & SOLUTION                                ║"
echo "║                    CI Pipeline Timeout Investigation                         ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

echo "Please answer the following questions based on your investigation:"
echo ""

# TSE Name for tracking
echo "👤 What's your name? (for tracking your submission)"
read -p "   Your name: " tse_name

# Question 1: Root Cause
echo ""
echo "1️⃣  What do you think is the root cause of the CI pipeline failure?"
echo "   (Describe what you found in the customer data)"
read -p "   Your answer: " root_cause

# Question 2: Solution
echo ""
echo "2️⃣  What solution would you recommend to fix this issue?"
echo "   (How would you resolve the problem?)"
read -p "   Your solution: " solution

# Save TSE Analysis
echo ""
echo "💾 Saving your analysis..."
cat > tse-analysis-$(date +%Y%m%d-%H%M%S).txt << EOF
TSE ANALYSIS - CI Pipeline Timeout
Generated: $(date)
TSE Name: $tse_name
=====================================

ROOT CAUSE:
$root_cause

PROPOSED SOLUTION:
$solution

=====================================
EOF

echo "✅ Analysis saved to: tse-analysis-$(date +%Y%m%d-%H%M%S).txt"
echo ""
echo "🎯 Great work! Your analysis has been recorded."
echo "   The instructor will review your findings."
