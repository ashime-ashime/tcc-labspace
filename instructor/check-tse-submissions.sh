#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                    📊 TSE SUBMISSION TRACKER                                ║"
echo "║                    Check TSE Analysis Submissions                           ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Navigate to exercise directory
cd /workspace/exercises/exercise-1-ci-timeout

echo "🔍 Checking for TSE submissions..."
echo ""

# List all TSE analysis files
if ls tse-analysis-*.txt 1> /dev/null 2>&1; then
    echo "📋 Found TSE Submissions:"
    echo "========================="
    
    for file in tse-analysis-*.txt; do
        echo ""
        echo "📄 File: $file"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        
        # Extract TSE name and date
        tse_name=$(grep "TSE Name:" "$file" | cut -d: -f2 | xargs)
        generated=$(grep "Generated:" "$file" | cut -d: -f2- | xargs)
        
        echo "👤 TSE: $tse_name"
        echo "📅 Submitted: $generated"
        echo ""
        echo "📝 Analysis Summary:"
        echo "   Root Cause: $(grep -A 1 "ROOT CAUSE:" "$file" | tail -1)"
        echo "   Solution: $(grep -A 1 "PROPOSED SOLUTION:" "$file" | tail -1)"
        echo ""
    done
    
    echo "📊 Total Submissions: $(ls tse-analysis-*.txt | wc -l)"
    echo ""
    echo "💡 To view full analysis: cat <filename>"
    echo "💡 To view specific TSE: grep -A 10 'TSE Name: <name>' tse-analysis-*.txt"
    
else
    echo "❌ No TSE submissions found yet."
    echo "   TSEs need to run: ./analyze-issue.sh"
fi

echo ""
echo "🎯 Instructor can now review all TSE analyses!"
