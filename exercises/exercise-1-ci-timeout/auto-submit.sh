#!/bin/bash

echo "📤 Auto-submitting your analysis to GitHub..."

# Get the latest analysis file
ANALYSIS_FILE=$(ls -t tse-analysis-*.txt 2>/dev/null | head -n1)

if [ -z "$ANALYSIS_FILE" ]; then
    echo "❌ No analysis file found. Please run ./analyze-issue.sh first."
    exit 1
fi

echo "📄 Found analysis file: $ANALYSIS_FILE"

# Create submissions directory if it doesn't exist
mkdir -p ../../submissions/exercise-1

# Copy analysis file to submissions directory
cp "$ANALYSIS_FILE" "../../submissions/exercise-1/"

# Due to Docker container limitations, we'll create a submission marker
# The actual git operations will be handled outside the container
echo "✅ Analysis file prepared for submission: $ANALYSIS_FILE"
echo "📋 Your analysis has been saved to: submissions/exercise-1/$ANALYSIS_FILE"

# Create a submission marker file for external processing
echo "$ANALYSIS_FILE" > ../../submissions/exercise-1/.latest-submission

echo ""
echo "🎯 SUBMISSION COMPLETE!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Your analysis has been submitted successfully!"
echo "📊 The instructor can now review your submission."
echo "💡 Thank you for completing the TCC Support Lab!"
echo ""
