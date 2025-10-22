#!/bin/bash

echo "📤 Submitting TSE analysis to GitHub..."

# Check if we're in the right directory
if [ ! -d "submissions" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

# Check if there's a new submission
if [ ! -f "submissions/exercise-1/.latest-submission" ]; then
    echo "❌ No new submissions found"
    exit 1
fi

# Get the latest submission file
SUBMISSION_FILE=$(cat submissions/exercise-1/.latest-submission)
echo "📄 Processing submission: $SUBMISSION_FILE"

# Switch to submissions branch
git checkout submissions

# Add the submission file
git add submissions/exercise-1/"$SUBMISSION_FILE"

# Commit with TSE name and timestamp
TSE_NAME=$(echo "$SUBMISSION_FILE" | sed 's/tse-analysis-\([^-]*\)-.*/\1/')
COMMIT_MSG="TSE Analysis Submission - $TSE_NAME - $(date +%Y%m%d-%H%M%S)"

git commit -m "$COMMIT_MSG"

# Push to GitHub
git push origin submissions

# Clean up the marker file
rm submissions/exercise-1/.latest-submission

echo "✅ Submission successfully pushed to GitHub!"
echo "📊 View submissions at: https://github.com/ashime-ashime/tcc-labspace/tree/submissions"
echo ""
echo "🎯 TSE Analysis submitted by: $TSE_NAME"
echo "📅 Timestamp: $(date)"
echo "📁 File: $SUBMISSION_FILE"
