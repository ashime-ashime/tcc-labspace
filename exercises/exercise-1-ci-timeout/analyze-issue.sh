#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                    🔍 TSE ANALYSIS & SOLUTION                                ║"
echo "║                    CI Pipeline Timeout Investigation                         ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

echo "Please answer the following questions based on your investigation:"
echo ""

# Question 1: Root Cause
echo "1️⃣  What do you think is the root cause of the CI pipeline failure?"
echo "   (Describe what you found in the customer data)"
read -p "   Your answer: " root_cause

# Question 2: Solution
echo ""
echo "2️⃣  What solution would you recommend to fix this issue?"
echo "   (How would you resolve the problem?)"
read -p "   Your solution: " solution

# Question 3: Customer Response
echo ""
echo "3️⃣  What would you tell the customer in your response?"
echo "   (Draft your professional customer communication)"
read -p "   Your response: " customer_response

# Question 4: Confidence Level
echo ""
echo "4️⃣  How confident are you in your analysis? (1-10)"
read -p "   Confidence level: " confidence

# Save TSE Analysis
echo ""
echo "💾 Saving your analysis..."
cat > tse-analysis-$(date +%Y%m%d-%H%M%S).txt << EOF
TSE ANALYSIS - CI Pipeline Timeout
Generated: $(date)
=====================================

ROOT CAUSE:
$root_cause

PROPOSED SOLUTION:
$solution

CUSTOMER RESPONSE:
$customer_response

CONFIDENCE LEVEL: $confidence/10

=====================================
EOF

echo "✅ Analysis saved to: tse-analysis-$(date +%Y%m%d-%H%M%S).txt"
echo ""
echo "🎯 Great work! Your analysis has been recorded."
echo "   The instructor will review your findings."
