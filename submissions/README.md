# TSE Submissions

This directory contains all TSE analysis submissions for the TCC Support Labs.

## Structure

```
submissions/
├── exercise-1/          # Exercise 1: CI Pipeline Timeout submissions
├── exercise-2/          # Exercise 2: (Future exercise) submissions
└── README.md           # This file
```

## How to View Submissions

### For Instructors:
```bash
# Switch to submissions branch
git checkout submissions

# View all submissions for Exercise 1
ls -la submissions/exercise-1/

# View a specific TSE's analysis
cat submissions/exercise-1/tse-analysis-[name]-[timestamp].txt
```

### For TSEs:
Your analysis submissions are automatically saved here when you complete the exercise using the analysis script.

## File Naming Convention

TSE analysis files follow this format:
`tse-analysis-[TSE-NAME]-[YYYYMMDD-HHMMSS].txt`

Example:
- `tse-analysis-john-doe-20250122-1430.txt`
- `tse-analysis-jane-smith-20250122-1505.txt`

## Submission Process

1. TSE completes the exercise analysis
2. TSE runs `./analyze-issue.sh` script
3. Analysis is automatically saved and submitted to this branch
4. Instructor can review submissions in this directory
