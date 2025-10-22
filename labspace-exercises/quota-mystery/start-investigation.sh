#!/bin/bash

# Interactive TSE Investigation Game Launcher
# Transforms the lab into an engaging mystery-solving experience

echo "🎮 Welcome to The Quota Mystery - Interactive TSE Investigation Game!"
echo "=================================================================="
echo ""
echo "🕵️‍♂️ You are a TSE detective solving a customer's TCC CI/CD failure"
echo "🎯 Your mission: Find the root cause and propose a solution"
echo "📊 Earn points by discovering clues and solving the mystery"
echo ""
echo "🎮 GAME FEATURES:"
echo "   • Interactive investigation paths"
echo "   • Progressive clue discovery" 
echo "   • Educational insights with each finding"
echo "   • Scoring system and progress tracking"
echo "   • Real diagnostic commands with mock API"
echo ""
echo "🚀 Ready to start your investigation?"
echo ""

read -p "Press Enter to begin the mystery... " 

# Start the interactive investigation engine
python3 .investigation-engine.py
