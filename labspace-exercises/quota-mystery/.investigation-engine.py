#!/usr/bin/env python3
"""
Enhanced Interactive TSE Investigation Engine
Complete TSE training simulation with customer analysis, investigation toolbox, and real outputs
"""

import json
import os
import sys
from datetime import datetime

class EnhancedInvestigationEngine:
    def __init__(self):
        self.clues_found = []
        self.score = 0
        self.max_score = 150
        self.max_clues = 6
        self.game_state = 'customer_analysis'  # customer_analysis, investigation_preview, active_investigation, solution_phase
        
        # Customer scenario data
        self.customer_scenario = {
            "company": "Enterprise Development Team",
            "priority": "HIGH - Blocking deployments",
            "timeline": "Started 48 hours ago",
            "issue": "GitHub Actions CI pipeline timing out with Testcontainers Cloud",
            "customer_says": "Local works fine, but CI fails",
            "customer_tried": "Regenerated service account token"
        }

        # Customer ticket details
        self.customer_ticket = """
📞 SUPPORT TICKET #TCC-2025-001
================================

Subject: GitHub Actions CI pipeline timeout with Testcontainers Cloud
Priority: High - Blocking deployments
Customer: Enterprise Development Team
Reported: 48 hours ago

Description:
Our CI/CD pipeline started failing 48 hours ago. The GitHub Actions workflow 
that sets up Testcontainers Cloud is timing out after approximately 2 minutes. 
We've attempted to resolve this by regenerating our service account token, 
but the issue persists.

Our local development environment works perfectly - tests run without issues 
when executed from developer machines. However, the same tests fail in our 
GitHub Actions environment.

Technical Details:
- Pipeline fails during TCC setup phase
- Timeout occurs before any test execution begins
- No recent changes to our Testcontainers configuration
- Same tests work locally with Docker Desktop

Business Impact:
- Blocking our deployment pipeline - can't release new features
- Affecting release schedule - quarterly update delayed
- Developer productivity - team can't validate changes in CI

What We've Tried:
- Regenerated service account token
- Checked TCC service status (operational)
- Verified network connectivity (no issues)
- Restarted GitHub Actions runners (no effect)
"""

        # Customer analysis quiz
        self.analysis_quiz = {
            "question": "Based on your analysis of the customer ticket, what's your initial hypothesis?",
            "options": {
                "A": {
                    "text": "Authentication/Token issue",
                    "insight": "Good thinking! Token regeneration suggests auth problems, but this might be a red herring.",
                    "points": 5
                },
                "B": {
                    "text": "Quota/Billing problem",
                    "insight": "Excellent insight! The '48 hours ago' timeline and local vs CI difference strongly suggests quota issues.",
                    "points": 15
                },
                "C": {
                    "text": "Network connectivity issue",
                    "insight": "Reasonable thought, but customer already verified network connectivity.",
                    "points": 3
                },
                "D": {
                    "text": "Configuration error",
                    "insight": "Possible, but customer says no recent configuration changes.",
                    "points": 7
                },
                "E": {
                    "text": "Service outage",
                    "insight": "Customer already checked - TCC service is operational.",
                    "points": 2
                }
            }
        }

        # Investigation toolbox with commands and expected outputs
        self.investigation_tools = {
            "1": {
                "name": "GitHub Actions Workflow Analyzer",
                "description": "Examine the broken CI configuration file",
                "command": "cat customer-report/broken-repo/.github/workflows/test.yml",
                "expected_output": """name: Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
      - name: Run Tests
        run: npm test""",
                "analysis_tip": "Notice what's missing? No testcontainers-cloud-setup-action!",
                "clue": "workflow_missing_setup",
                "points": 15,
                "key": "workflow_missing_setup"
            },
            "2": {
                "name": "Failure Logs Analyzer",
                "description": "Check GitHub Actions execution logs for specific errors",
                "command": "cat customer-report/github-actions-logs.txt",
                "expected_output": """[2025-01-09 10:15:23] Starting GitHub Actions workflow
[2025-01-09 10:15:24] Checking out repository code
[2025-01-09 10:15:25] Setting up Node.js environment
[2025-01-09 10:15:26] Attempting Testcontainers Cloud setup...
[2025-01-09 10:17:30] ERROR: Testcontainers Cloud setup failed: Quota exceeded
[2025-01-09 10:17:30] Workflow terminated due to timeout""",
                "analysis_tip": "The logs show 'Quota exceeded' error during TCC setup - this is the smoking gun!",
                "clue": "logs_quota_exceeded",
                "points": 20,
                "key": "logs_quota_exceeded"
            },
            "3": {
                "name": "TCC Service Health Check",
                "description": "Verify if the Testcontainers Cloud service is operational",
                "command": "curl http://localhost:8080/v1/health",
                "expected_output": """{
  "status": "operational",
  "timestamp": "2025-01-09T10:15:30Z",
  "version": "1.0.0"
}""",
                "analysis_tip": "Service is operational - this rules out a TCC service outage.",
                "clue": "api_health_ok",
                "points": 10,
                "key": "api_health_ok"
            },
            "4": {
                "name": "Account Usage Inspector",
                "description": "Investigate quota and usage patterns using the mock API",
                "command": 'curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/usage',
                "expected_output": """{
  "free_tier_minutes": 50,
  "current_month_usage": 52,
  "quota_exceeded": true,
  "quota_reset": "never",
  "last_successful_ci": "2025-01-08T14:22:00Z",
  "quota_exhausted_date": "2025-01-09T00:00:00Z"
}""",
                "analysis_tip": "🚨 SMOKING GUN! Usage is 52/50 minutes - quota exceeded! This is the root cause!",
                "clue": "api_usage_exceeded",
                "points": 30,
                "key": "api_usage_exceeded"
            },
            "5": {
                "name": "Account Details Inspector",
                "description": "Examine customer's TCC account configuration",
                "command": 'curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/account',
                "expected_output": """{
  "org_id": "3294",
  "plan_type": "trial_legacy",
  "status": "active",
  "billing_model": "separate_tcc_billing",
  "docker_pro_plan": "legacy_subscription",
  "tcc_included": false
}""",
                "analysis_tip": "Legacy trial plan with separate TCC billing - explains the limitations and quota restrictions.",
                "clue": "api_account_details",
                "points": 15,
                "key": "api_account_details"
            },
            "6": {
                "name": "Static Account Data Review",
                "description": "Review the detailed account information file",
                "command": "cat customer-report/account-details.json",
                "expected_output": """{
  "org_id": "3294",
  "plan_type": "trial_legacy",
  "status": "active",
  "billing_model": "separate_tcc_billing",
  "quota_exceeded": true,
  "free_tier_minutes": 50,
  "current_month_usage": 52,
  "last_successful_ci": "2025-01-08T14:22:00Z",
  "quota_exhausted_date": "2025-01-09T00:00:00Z"
}""",
                "analysis_tip": "This corroborates the API findings - quota exceeded 48 hours ago, matching the customer's timeline!",
                "clue": "static_account_data",
                "points": 10,
                "key": "static_account_data"
            }
        }

        # Solution options
        self.solutions = {
            "1": {
                "title": "Upgrade TCC Plan",
                "description": "Recommend upgrading to a Docker Business or Team plan for more TCC minutes",
                "correct": True,
                "points": 20
            },
            "2": {
                "title": "Optimize CI Usage",
                "description": "Suggest optimizing CI workflows to reduce TCC minute consumption",
                "correct": True,
                "points": 15
            },
            "3": {
                "title": "Fix GitHub Actions Workflow",
                "description": "Add the missing testcontainers-cloud-setup-action to the workflow",
                "correct": False,  # This is a secondary issue, not the root cause
                "points": 5
            },
            "4": {
                "title": "Switch to Local Testing",
                "description": "Advise running tests locally as it doesn't consume TCC minutes",
                "correct": True,
                "points": 10
            }
        }

    def start_investigation(self):
        """Start the enhanced investigation experience"""
        self.clear_screen()
        self.print_banner()
        
        # Phase 1: Customer Analysis
        self.customer_analysis_phase()
        
        # Phase 2: Investigation Toolbox Preview
        self.investigation_preview_phase()
        
        # Phase 3: Active Investigation
        self.active_investigation_phase()
        
        # Phase 4: Solution Proposal
        self.solution_phase()

    def print_banner(self):
        """Print the investigation banner"""
        print("🕵️‍♂️ Welcome to The Quota Mystery - Enhanced TSE Investigation")
        print("=" * 65)
        print()
        print("🎯 Mission: Solve a customer's TCC CI/CD failure")
        print("📊 Score: {}/{}".format(self.score, self.max_score))
        print("🔍 Clues Found: {}/{}".format(len(self.clues_found), self.max_clues))
        print()

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')

    def customer_analysis_phase(self):
        """Phase 1: Customer Analysis"""
        print("📋 PHASE 1: CUSTOMER ANALYSIS")
        print("=" * 35)
        print()
        
        # Show customer ticket
        print("📞 CUSTOMER TICKET:")
        print("-" * 20)
        print(self.customer_ticket)
        print()
        
        input("⏎ Press Enter to continue to analysis quiz...")
        print()
        
        # Customer analysis quiz
        print("🧠 INITIAL ASSESSMENT QUIZ:")
        print("-" * 30)
        print(self.analysis_quiz["question"])
        print()
        
        for option, data in self.analysis_quiz["options"].items():
            print(f"{option}. {data['text']}")
        
        print()
        
        while True:
            choice = input("🎯 Enter your hypothesis (A-E): ").strip().upper()
            if choice in self.analysis_quiz["options"]:
                selected = self.analysis_quiz["options"][choice]
                self.score += selected["points"]
                
                print()
                print("💡 ANALYSIS INSIGHT:")
                print("-" * 20)
                print(selected["insight"])
                print(f"📊 Points earned: {selected['points']}")
                print(f"📊 Total score: {self.score}/{self.max_score}")
                break
            else:
                print("❌ Please enter A, B, C, D, or E")
        
        print()
        input("⏎ Press Enter to continue to Investigation Toolbox...")

    def investigation_preview_phase(self):
        """Phase 2: Investigation Toolbox Preview"""
        self.clear_screen()
        print("🔧 PHASE 2: INVESTIGATION TOOLBOX")
        print("=" * 35)
        print()
        print("Here are your diagnostic tools. Each shows exactly what command")
        print("you'll run and what output to expect. Plan your investigation")
        print("strategy, then start when ready!")
        print()
        
        for tool_id, tool in self.investigation_tools.items():
            print(f"🔍 Tool {tool_id}: {tool['name']}")
            print(f"   💡 What it reveals: {tool['description']}")
            print(f"   💻 Command: {tool['command']}")
            print(f"   📄 Expected output: {tool['expected_output'][:100]}{'...' if len(tool['expected_output']) > 100 else ''}")
            print(f"   🔍 Analysis tip: {tool['analysis_tip']}")
            print(f"   🎯 When to use: {'Early investigation' if tool_id in ['1', '2'] else 'After initial findings' if tool_id in ['3', '4'] else 'Final confirmation'}")
            print()
        
        print("🎯 INVESTIGATION STRATEGY TIPS:")
        print("-" * 35)
        print("• Start with tools 1-2 (workflow and logs) for initial context")
        print("• Use tool 3 (health check) to rule out service issues")
        print("• Tools 4-5 (usage/account) will reveal the root cause")
        print("• Tool 6 (static data) provides final confirmation")
        print()
        
        input("⏎ Press Enter to start active investigation...")

    def active_investigation_phase(self):
        """Phase 3: Active Investigation"""
        self.clear_screen()
        print("🕵️‍♂️ PHASE 3: ACTIVE INVESTIGATION")
        print("=" * 35)
        print()
        print("Now it's time to investigate! Run the diagnostic tools in any")
        print("order you prefer. You can always go back to review customer")
        print("information or the toolbox.")
        print()
        
        while len(self.clues_found) < self.max_clues:
            self.show_investigation_menu()
            
            choice = input(f"\n🎯 What would you like to investigate? (1-6, 'help', 'status', 'customer', 'toolbox', 'solve'): ").strip().lower()
            
            if choice == 'help':
                self.show_help()
            elif choice == 'status':
                self.show_status()
            elif choice == 'customer':
                self.show_customer_info()
            elif choice == 'toolbox':
                self.show_toolbox()
            elif choice == 'solve':
                if len(self.clues_found) >= 4:
                    return  # Move to solution phase
                else:
                    print("🔍 You need to find more clues before proposing a solution! (Need at least 4 clues)")
            elif choice.isdigit() and 1 <= int(choice) <= 6:
                tool_id = choice
                if tool_id not in self.clues_found:
                    self.execute_investigation_tool(tool_id)
                else:
                    print("ℹ️  You've already investigated this tool!")
            else:
                print("❌ Invalid choice. Try again.")
            
            input("\n⏎ Press Enter to continue...")

    def show_investigation_menu(self):
        """Show the investigation menu"""
        print("\n🔍 INVESTIGATION TOOLS:")
        print("-" * 25)
        
        for tool_id, tool in self.investigation_tools.items():
            status = "✅" if tool_id in self.clues_found else "🔍"
            print(f"{tool_id}. {status} {tool['name']}")
            print(f"   💭 {tool['description']}")
        
        print("\n📊 INVESTIGATION STATUS:")
        print(f"   Score: {self.score}/{self.max_score}")
        print(f"   Clues: {len(self.clues_found)}/{self.max_clues}")
        print(f"   Progress: {len(self.clues_found)/self.max_clues*100:.0f}%")

    def execute_investigation_tool(self, tool_id):
        """Execute an investigation tool"""
        tool = self.investigation_tools[tool_id]
        
        print(f"\n🔍 {tool['name']}")
        print("=" * 50)
        print(f"💭 {tool['description']}")
        print()
        
        print("🛠️  Command to run:")
        print(f"   {tool['command']}")
        print()
        
        # Show expected output
        print("📄 Expected output:")
        print("-" * 20)
        print(tool['expected_output'])
        print()
        
        # Show analysis tip
        print("🔍 Analysis tip:")
        print(f"   {tool['analysis_tip']}")
        print()
        
        # Add clue and score
        self.clues_found.append(tool_id)
        self.score += tool['points']
        
        print("🎯 CLUE DISCOVERED!")
        print("=" * 20)
        print(f"💡 {tool['analysis_tip']}")
        print(f"📊 Points earned: {tool['points']}")
        print(f"📊 Total score: {self.score}/{self.max_score}")
        
        # Check if this is the smoking gun
        if tool_id == "4":  # Account Usage Inspector
            print()
            print("🚨 ROOT CAUSE IDENTIFIED!")
            print("   You've found the smoking gun - quota exceeded!")
            print("   This explains why local works but CI fails.")
            print("   Local tests don't count against TCC quota!")

    def solution_phase(self):
        """Phase 4: Solution Proposal"""
        self.clear_screen()
        print("🎯 PHASE 4: SOLUTION PROPOSAL")
        print("=" * 35)
        print()
        print("Based on your investigation, what solutions would you propose to the customer?")
        print("You can select multiple solutions:")
        print()
        
        for sol_id, solution in self.solutions.items():
            print(f"{sol_id}. {solution['title']}")
            print(f"   💭 {solution['description']}")
        
        print()
        
        chosen_solutions = []
        while True:
            choice_input = input("🎯 Enter solution numbers (e.g., '1 2 4'), or 'done' to finish: ").strip()
            if choice_input.lower() == 'done':
                break
            try:
                choices = [c.strip() for c in choice_input.split()]
                for c in choices:
                    if c in self.solutions and c not in chosen_solutions:
                        chosen_solutions.append(c)
                    elif c not in self.solutions:
                        print(f"❌ Invalid solution number: {c}")
            except:
                print("❌ Invalid input. Please enter numbers or 'done'.")
        
        print()
        print("🎯 EVALUATING YOUR SOLUTIONS:")
        print("=" * 35)
        
        solution_score = 0
        for sol_id in chosen_solutions:
            solution = self.solutions[sol_id]
            if solution["correct"]:
                solution_score += solution["points"]
                print(f"✅ Excellent Solution: {solution['title']} (+{solution['points']} points)")
            else:
                print(f"⚠️  Partial Solution: {solution['title']} (+{solution['points']} points)")
                print("   (This addresses a secondary issue, not the root cause)")
                solution_score += solution["points"]
        
        self.score += solution_score
        
        print()
        print("🎉 INVESTIGATION COMPLETE!")
        print("=" * 25)
        print(f"📊 Final Score: {self.score}/{self.max_score}")
        print(f"🔍 Clues Found: {len(self.clues_found)}/{self.max_clues}")
        print()
        print("💼 CUSTOMER COMMUNICATION:")
        print("-" * 25)
        print("Based on your investigation, you should communicate to the customer:")
        print("• Root cause: TCC quota exceeded (52/50 minutes used)")
        print("• Why local works: Local tests don't count against quota")
        print("• Solutions: Upgrade plan, optimize usage, or use local testing")
        print("• Timeline: Issue started when quota was exhausted 48 hours ago")
        print()
        print("🎯 Great detective work! You've successfully solved The Quota Mystery!")

    def show_help(self):
        """Show help information"""
        print("\n📚 INVESTIGATION HELP:")
        print("-" * 25)
        print("🎯 Goal: Find why CI fails but local works")
        print("🔍 Method: Use diagnostic tools to gather evidence")
        print("📊 Scoring: Each tool gives points when discovered")
        print("💡 Tips: Follow the evidence trail systematically")
        print("🔄 Freedom: Go back to customer info or toolbox anytime")

    def show_status(self):
        """Show current investigation status"""
        print(f"\n📊 INVESTIGATION STATUS:")
        print(f"   Score: {self.score}/{self.max_score}")
        print(f"   Clues Found: {len(self.clues_found)}/{self.max_clues}")
        print(f"   Root Cause: {'✅ Found' if '4' in self.clues_found else '🔍 Still investigating'}")
        
        if self.clues_found:
            print(f"\n🔍 Tools Used:")
            for tool_id in self.clues_found:
                tool = self.investigation_tools[tool_id]
                print(f"   ✅ {tool['name']}")

    def show_customer_info(self):
        """Show customer information"""
        print("\n📞 CUSTOMER INFORMATION:")
        print("-" * 25)
        print(self.customer_ticket)

    def show_toolbox(self):
        """Show investigation toolbox"""
        print("\n🔧 INVESTIGATION TOOLBOX:")
        print("-" * 25)
        for tool_id, tool in self.investigation_tools.items():
            status = "✅ Used" if tool_id in self.clues_found else "🔍 Available"
            print(f"{tool_id}. {status} {tool['name']}")
            print(f"   💻 {tool['command']}")

def main():
    """Main function to start the enhanced investigation"""
    engine = EnhancedInvestigationEngine()
    engine.start_investigation()

if __name__ == "__main__":
    main()