#!/usr/bin/env python3
"""
Interactive TSE Investigation Engine
Transforms the lab into an engaging mystery-solving experience
"""

import json
import os
import sys
from datetime import datetime

class InvestigationEngine:
    def __init__(self):
        self.clues_found = []
        self.investigation_path = []
        self.score = 0
        self.max_score = 100
        
        # Investigation states
        self.states = {
            "initial": True,
            "workflow_analyzed": False,
            "api_diagnosed": False,
            "account_reviewed": False,
            "root_cause_identified": False,
            "solution_proposed": False
        }
        
        # Available investigation actions
        self.actions = {
            "workflow": {
                "name": "Analyze GitHub Actions Workflow",
                "description": "Examine the broken CI configuration",
                "command": "cat customer-report/broken-repo/.github/workflows/test.yml",
                "clue": "workflow_analysis"
            },
            "logs": {
                "name": "Review Failure Logs", 
                "description": "Check GitHub Actions execution logs",
                "command": "cat customer-report/github-actions-logs.txt",
                "clue": "log_analysis"
            },
            "api_health": {
                "name": "Test TCC Service Health",
                "description": "Verify if TCC service is operational",
                "command": "curl http://localhost:8080/v1/health",
                "clue": "api_health"
            },
            "api_usage": {
                "name": "Check Account Usage",
                "description": "Investigate quota and usage patterns",
                "command": "curl -H 'Authorization: Bearer tcc-lab-token-12345' http://localhost:8080/v1/usage",
                "clue": "api_usage"
            },
            "api_account": {
                "name": "Review Account Details",
                "description": "Examine customer's TCC account configuration",
                "command": "curl -H 'Authorization: Bearer tcc-lab-token-12345' http://localhost:8080/v1/account",
                "clue": "api_account"
            },
            "account_data": {
                "name": "Analyze Account Data",
                "description": "Review detailed account information",
                "command": "cat customer-report/account-details.json",
                "clue": "account_data"
            }
        }
        
        # Clue responses with educational insights
        self.clue_responses = {
            "workflow_analysis": {
                "found": True,
                "insight": "🔍 The workflow is missing the TCC setup action! This explains the timeout.",
                "education": "TCC requires a setup action to initialize the cloud environment before tests run.",
                "score": 15,
                "next_hints": ["api_health", "logs"]
            },
            "log_analysis": {
                "found": True,
                "insight": "📋 Logs show timeout during TCC initialization, not test execution.",
                "education": "This indicates the issue is in the TCC setup phase, not the actual tests.",
                "score": 10,
                "next_hints": ["api_health", "workflow"]
            },
            "api_health": {
                "found": True,
                "insight": "✅ TCC service is operational - this rules out connectivity issues.",
                "education": "When health checks pass, the issue is usually configuration or quota-related.",
                "score": 10,
                "next_hints": ["api_usage", "api_account"]
            },
            "api_usage": {
                "found": True,
                "insight": "🚨 SMOKING GUN! Quota exceeded: 52/50 minutes used!",
                "education": "TCC free tier has a 50-minute monthly limit. Once exceeded, CI runs will fail.",
                "score": 25,
                "next_hints": ["api_account", "account_data"]
            },
            "api_account": {
                "found": True,
                "insight": "🏢 Legacy trial plan with separate TCC billing - explains the limitations.",
                "education": "Legacy plans don't include TCC minutes, so all usage counts against free tier.",
                "score": 15,
                "next_hints": ["account_data"]
            },
            "account_data": {
                "found": True,
                "insight": "📊 Account history shows quota exhausted 48 hours ago - matches timeline!",
                "education": "Local tests work because they don't count against TCC quota.",
                "score": 15,
                "next_hints": []
            }
        }

    def start_investigation(self):
        """Start the interactive investigation"""
        self.clear_screen()
        print("🕵️‍♂️ Welcome to The Quota Mystery - Interactive TSE Investigation")
        print("=" * 60)
        print()
        print("🎯 Mission: Solve a customer's TCC CI/CD failure")
        print("📊 Score: {}/{}".format(self.score, self.max_score))
        print("🔍 Clues Found: {}/6".format(len(self.clues_found)))
        print()
        
        # Show customer scenario
        self.show_customer_scenario()
        
        # Main investigation loop
        while not self.states["solution_proposed"]:
            self.show_investigation_menu()
            choice = input("\n🎯 What would you like to investigate? (1-6, 'help', 'status', 'quit'): ").strip()
            
            if choice.lower() == 'quit':
                print("\n👋 Investigation abandoned. The customer is still waiting for help!")
                return
            elif choice.lower() == 'help':
                self.show_help()
                continue
            elif choice.lower() == 'status':
                self.show_status()
                continue
            elif choice.isdigit() and 1 <= int(choice) <= len(self.get_available_actions()):
                action_key = list(self.get_available_actions().keys())[int(choice) - 1]
                self.execute_action(action_key)
            else:
                print("❌ Invalid choice. Try again.")
                
            input("\n⏎ Press Enter to continue...")

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')

    def show_customer_scenario(self):
        """Display the customer scenario"""
        print("📞 CUSTOMER SCENARIO:")
        print("-" * 30)
        print("🏢 Enterprise Development Team")
        print("🚨 Priority: HIGH - Blocking deployments")
        print("⏰ Timeline: Started 48 hours ago")
        print("📋 Issue: GitHub Actions CI pipeline timing out")
        print("🤔 Customer says: 'Local works fine, but CI fails'")
        print("💭 Customer tried: Regenerated service account token")
        print()
        print("🎯 Your mission: Find the root cause and propose a solution!")
        print()

    def get_available_actions(self):
        """Get available investigation actions based on current state"""
        available = {}
        
        # Always available actions
        for key, action in self.actions.items():
            if key not in self.clues_found:
                available[key] = action
                
        return available

    def show_investigation_menu(self):
        """Show the investigation menu"""
        available = self.get_available_actions()
        
        print("\n🔍 INVESTIGATION OPTIONS:")
        print("-" * 30)
        
        for i, (key, action) in enumerate(available.items(), 1):
            status = "✅" if key in self.clues_found else "🔍"
            print(f"{i}. {status} {action['name']}")
            print(f"   💭 {action['description']}")
            
        print("\n📊 INVESTIGATION STATUS:")
        print(f"   Score: {self.score}/{self.max_score}")
        print(f"   Clues: {len(self.clues_found)}/6")
        print(f"   Progress: {len(self.clues_found)/6*100:.0f}%")

    def execute_action(self, action_key):
        """Execute an investigation action"""
        action = self.actions[action_key]
        
        print(f"\n🔍 {action['name']}")
        print("-" * 40)
        print(f"💭 {action['description']}")
        print()
        
        # Show the command
        print("🛠️  Command to run:")
        print(f"   {action['command']}")
        print()
        
        # Ask if they want to run it
        run_it = input("🤔 Do you want to run this command? (y/n): ").strip().lower()
        
        if run_it == 'y':
            print(f"\n⚡ Executing: {action['command']}")
            print("📋 (Command output would appear here)")
            print()
            
            # Simulate command execution and show clue
            self.process_clue(action_key)
        else:
            print("⏭️  Skipped this investigation step.")

    def process_clue(self, clue_key):
        """Process a found clue"""
        if clue_key in self.clues_found:
            print("ℹ️  You've already investigated this!")
            return
            
        clue = self.clue_responses.get(clue_key)
        if not clue:
            print("❓ Interesting finding, but no specific insight available.")
            return
            
        self.clues_found.append(clue_key)
        self.score += clue.get('score', 0)
        
        print("🎯 CLUE DISCOVERED!")
        print("=" * 20)
        print(f"💡 {clue['insight']}")
        print()
        print("📚 Educational Insight:")
        print(f"   {clue['education']}")
        print()
        
        # Check if this reveals the root cause
        if clue_key == "api_usage":
            self.states["root_cause_identified"] = True
            print("🚨 ROOT CAUSE IDENTIFIED!")
            print("   You've found the smoking gun - quota exceeded!")
            print("   This explains why local works but CI fails.")
            print()
            
        # Show next recommended actions
        if clue.get('next_hints'):
            print("🔍 Recommended next steps:")
            for hint in clue['next_hints']:
                if hint not in self.clues_found:
                    action = self.actions[hint]
                    print(f"   • {action['name']}")
            print()
            
        # Check if ready for solution
        if len(self.clues_found) >= 4:
            self.offer_solution_phase()

    def offer_solution_phase(self):
        """Offer to move to solution phase"""
        print("🎉 INVESTIGATION MILESTONE REACHED!")
        print("=" * 35)
        print(f"📊 Score: {self.score}/{self.max_score}")
        print(f"🔍 Clues: {len(self.clues_found)}/6")
        print()
        
        if self.states["root_cause_identified"]:
            print("✅ You've identified the root cause!")
            proceed = input("🤔 Ready to propose solutions? (y/n): ").strip().lower()
            if proceed == 'y':
                self.solution_phase()
        else:
            print("🔍 You have good evidence, but consider investigating more.")
            print("💡 Hint: Look for quota-related information...")

    def solution_phase(self):
        """Handle the solution proposal phase"""
        print("\n🎯 SOLUTION PROPOSAL PHASE")
        print("=" * 30)
        print("📋 Based on your investigation, propose solutions:")
        print()
        print("1. 💰 Upgrade to paid plan (more TCC minutes)")
        print("2. 🔧 Optimize CI usage (reduce test time)")
        print("3. 🏠 Use local testing for development")
        print("4. 📞 Contact sales for enterprise plan")
        print()
        
        choice = input("🎯 Which solution would you recommend? (1-4): ").strip()
        
        if choice in ['1', '2', '3', '4']:
            self.score += 10
            print(f"\n✅ Solution proposed! Final score: {self.score}/{self.max_score}")
            print("🎉 Investigation complete!")
            self.states["solution_proposed"] = True
        else:
            print("❌ Please select a valid solution option.")

    def show_help(self):
        """Show help information"""
        print("\n📚 INVESTIGATION HELP:")
        print("-" * 25)
        print("🎯 Goal: Find why CI fails but local works")
        print("🔍 Method: Gather evidence through investigation")
        print("📊 Scoring: Each clue gives points")
        print("💡 Tips: Follow the evidence trail")
        print("🎮 Commands: Use 'status' to see progress")

    def show_status(self):
        """Show current investigation status"""
        print(f"\n📊 INVESTIGATION STATUS:")
        print(f"   Score: {self.score}/{self.max_score}")
        print(f"   Clues Found: {len(self.clues_found)}")
        print(f"   Root Cause: {'✅ Found' if self.states['root_cause_identified'] else '🔍 Still investigating'}")
        print(f"   Solution: {'✅ Proposed' if self.states['solution_proposed'] else '⏳ In progress'}")
        
        if self.clues_found:
            print(f"\n🔍 Clues Discovered:")
            for clue in self.clues_found:
                action = self.actions[clue]
                print(f"   ✅ {action['name']}")

def main():
    """Main function to start the investigation"""
    engine = InvestigationEngine()
    engine.start_investigation()

if __name__ == "__main__":
    main()
