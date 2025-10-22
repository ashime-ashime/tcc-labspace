#!/bin/bash

# Traditional Mode Launcher
# Provides the original step-by-step investigation experience

echo "📋 Starting Traditional Investigation Mode"
echo "=========================================="
echo ""
echo "This mode provides the original step-by-step investigation approach."
echo "Perfect for TSEs who prefer guided instructions over interactive gameplay."
echo ""
echo "🔍 Traditional Investigation Options:"
echo "   • Step-by-step investigation guide"
echo "   • Manual diagnostic command execution"
echo "   • Structured learning approach"
echo "   • No scoring or game elements"
echo ""

read -p "Press Enter to start traditional investigation... "

# Navigate to exercise and show traditional README
cd /workspace/labspace-exercises/quota-mystery
echo ""
echo "📚 Traditional Investigation Guide:"
echo "=================================="
echo ""
cat README.md
