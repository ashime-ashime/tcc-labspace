#!/usr/bin/env python3
"""
Complete Enhanced Interactive TSE Investigation Engine
Real TSE training simulation with customer analysis, real command execution, and evidence-based solutions
"""

import json
import os
import sys
from datetime import datetime

class CompleteEnhancedInvestigationEngine:
    def __init__(self):
        self.clues_found = []
        self.score = 0
        self.max_score = 200
        self.max_clues = 6  # Essential clues only
        self.game_state = 'customer_analysis'
        self.quiz_attempts = 0
        self.max_quiz_attempts = 2
        
        # Customer scenario data
        self.customer_scenario = {
            "company": "Enterprise Development Team",
            "priority": "HIGH - Blocking deployments",
            "timeline": "Started 48 hours ago",
            "issue": "GitHub Actions CI pipeline timing out with Testcontainers Cloud",
            "customer_says": "Local works fine, but CI fails",
            "customer_tried": "Regenerated service account token"
        }

        # Complete customer ticket
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

        # Supporting documents for customer analysis (without spoiler insights)
        self.supporting_documents = [
            {
                "name": "GitHub Actions Workflow",
                "file": "customer-report/broken-repo/.github/workflows/test.yml",
                "preview": """name: Test Suite
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
                "key_insight": "Workflow configuration for CI/CD pipeline"
            },
            {
                "name": "Execution Logs",
                "file": "customer-report/github-actions-logs.txt",
                "preview": """[2025-01-09 10:15:23] Starting GitHub Actions workflow
[2025-01-09 10:15:26] Attempting Testcontainers Cloud setup...
[2025-01-09 10:17:30] ERROR: Testcontainers Cloud setup failed: Quota exceeded
[2025-01-09 10:17:30] Workflow terminated due to timeout""",
                "key_insight": "GitHub Actions execution timeline and error messages"
            },
            {
                "name": "Account Configuration",
                "file": "customer-report/account-details.json",
                "preview": """{
  "org_id": "3294",
  "plan_type": "trial_legacy",
  "status": "active",
  "billing_model": "separate_tcc_billing",
  "quota_exceeded": true,
  "free_tier_minutes": 50,
  "current_month_usage": 52
}""",
                "key_insight": "Customer account details and billing configuration"
            },
            {
                "name": "Usage Dashboard",
                "file": "customer-report/usage-dashboard-screenshot.txt",
                "preview": """TCC Usage Dashboard
===================
Free Tier Limit: 50 minutes
Current Usage: 52 minutes
Status: QUOTA EXCEEDED
Last Successful CI: 2025-01-08 14:22:00
Quota Exhausted: 2025-01-09 00:00:00""",
                "key_insight": "Usage statistics and quota information"
            }
        ]

        # Enhanced analysis quiz (now based on investigation evidence)
        self.analysis_quiz = {
            "question": "Based on your investigation findings, what's the root cause?",
            "options": {
                "A": {
                    "text": "Authentication/Token issue",
                    "insight": "Your investigation showed the token is valid and authentication works. This isn't the root cause.",
                    "points": 3
                },
                "B": {
                    "text": "Quota/Billing problem",
                    "insight": "🎯 EXCELLENT! Your investigation revealed quota exceeded (52/50 minutes) and legacy trial plan with separate billing. This is the root cause!",
                    "points": 20
                },
                "C": {
                    "text": "Network connectivity issue",
                    "insight": "Your health check investigation showed TCC service is operational and network is fine.",
                    "points": 2
                },
                "D": {
                    "text": "Configuration error",
                    "insight": "Good catch! Your workflow analysis revealed missing testcontainers-cloud-setup-action, but this is secondary to the quota issue.",
                    "points": 8
                },
                "E": {
                    "text": "Service outage",
                    "insight": "Your health check investigation confirmed TCC service is operational. Not the root cause.",
                    "points": 1
                }
            }
        }

        # Enhanced investigation tools (10 total: 6 essential + 4 red herrings)
        self.investigation_tools = {
            # Essential tools (must complete all 6)
            "1": {
                "name": "GitHub Actions Workflow Analyzer",
                "description": "Examine the broken CI configuration file",
                "command": "cat customer-report/broken-repo/.github/workflows/test.yml",
                "analysis_tip": "🔍 The workflow is missing the testcontainers-cloud-setup-action step! This explains the timeout during TCC setup.",
                "clue": "workflow_missing_setup",
                "points": 20,
                "is_essential": True
            },
            "2": {
                "name": "Failure Logs Analyzer",
                "description": "Check GitHub Actions execution logs for specific errors",
                "command": "cat customer-report/github-actions-logs.txt",
                "analysis_tip": "🚨 SMOKING GUN! Logs show 'ERROR: Testcontainers Cloud setup failed: Quota exceeded'. This is the root cause!",
                "clue": "logs_quota_exceeded",
                "points": 25,
                "is_essential": True
            },
            "3": {
                "name": "TCC Service Health Check",
                "description": "Verify if the Testcontainers Cloud service is operational",
                "command": "curl http://localhost:8080/v1/health",
                "analysis_tip": "✅ TCC service is operational - this rules out a service outage. The issue is elsewhere.",
                "clue": "api_health_ok",
                "points": 15,
                "is_essential": True
            },
            "4": {
                "name": "Account Usage Inspector",
                "description": "Investigate quota and usage patterns using the mock API",
                "command": 'curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/usage',
                "analysis_tip": "🎯 CONFIRMED! Usage is 52/50 minutes - quota exceeded! This explains why CI fails but local works.",
                "clue": "api_usage_exceeded",
                "points": 30,
                "is_essential": True
            },
            "5": {
                "name": "Account Details Inspector",
                "description": "Examine customer's TCC account configuration",
                "command": 'curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/account',
                "analysis_tip": "🏢 Legacy trial plan with separate TCC billing - explains the quota limitations and billing confusion.",
                "clue": "api_account_details",
                "points": 20,
                "is_essential": True
            },
            "6": {
                "name": "Static Account Data Review",
                "description": "Review the detailed account information file",
                "command": "cat customer-report/account-details.json",
                "analysis_tip": "📊 This corroborates the API findings - quota exceeded 48 hours ago, matching the customer's timeline perfectly!",
                "clue": "static_account_data",
                "points": 15,
                "is_essential": True
            },
            # Red herring tools (exploratory, no penalty)
            "7": {
                "name": "Network Connectivity Test",
                "description": "Test network connectivity to TCC services",
                "command": "curl -I https://api.testcontainers.cloud",
                "analysis_tip": "📡 Network connectivity is fine, but this doesn't solve the quota issue. Customer already verified this.",
                "clue": "network_connectivity_ok",
                "points": 0,
                "is_essential": False
            },
            "8": {
                "name": "Docker Version Check",
                "description": "Check Docker version and compatibility",
                "command": "docker --version",
                "analysis_tip": "🐳 Docker version is current, but this isn't related to TCC quota limits.",
                "clue": "docker_version_ok",
                "points": 0,
                "is_essential": False
            },
            "9": {
                "name": "GitHub Actions Runner Status",
                "description": "Check GitHub Actions runner configuration",
                "command": "echo 'GitHub Actions runners are operational'",
                "analysis_tip": "🏃 GitHub Actions runners are working fine. The issue is with TCC quota, not runner status.",
                "clue": "runner_status_ok",
                "points": 0,
                "is_essential": False
            },
            "10": {
                "name": "Service Account Token Validation",
                "description": "Validate the TCC service account token",
                "command": 'curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/account',
                "analysis_tip": "🔑 Token is valid and working, but customer already regenerated it. The issue is quota, not authentication.",
                "clue": "token_validation_ok",
                "points": 0,
                "is_essential": False
            }
        }

        # Enhanced solutions with evidence requirements
        self.solutions = {
            "1": {
                "title": "Upgrade TCC Plan",
                "description": "Recommend upgrading to a Docker Business or Team plan for more TCC minutes",
                "correct": True,
                "points": 30,
                "evidence_required": ["api_usage_exceeded", "api_account_details"],
                "explanation": "Based on your investigation: quota exceeded (52/50 minutes) and legacy trial plan with no included TCC minutes. Upgrade provides immediate quota relief and includes TCC minutes in the plan."
            },
            "2": {
                "title": "Optimize CI Usage",
                "description": "Suggest optimizing CI workflows to reduce TCC minute consumption",
                "correct": True,
                "points": 25,
                "evidence_required": ["api_usage_exceeded"],
                "explanation": "Your usage data shows 52 minutes consumed this month. Optimizing workflows (container reuse, parallel testing, selective test runs) can reduce consumption and extend current quota."
            },
            "3": {
                "title": "Switch to Local Testing",
                "description": "Advise running tests locally as it doesn't consume TCC minutes",
                "correct": True,
                "points": 20,
                "evidence_required": ["api_account_details"],
                "explanation": "Your account investigation revealed local execution is unlimited (customer infrastructure). This provides immediate relief while planning long-term solutions like plan upgrades."
            },
            "4": {
                "title": "Fix GitHub Actions Workflow",
                "description": "Add the missing testcontainers-cloud-setup-action to the workflow",
                "correct": True,
                "points": 15,
                "evidence_required": ["workflow_missing_setup"],
                "explanation": "This addresses a secondary issue - the missing TCC setup action. However, even with this fix, the workflow will still fail due to quota exceeded. Fix both issues for complete resolution."
            },
            "5": {
                "title": "Regenerate Service Account Token",
                "description": "Generate a new TCC service account token",
                "correct": False,
                "points": 0,
                "explanation": "Customer already tried this. Your logs analysis showed 'Quota exceeded' error, not authentication issues. Token regeneration won't solve quota problems - the token is working fine."
            },
            "6": {
                "title": "Contact TCC Support",
                "description": "Escalate to Testcontainers Cloud support team",
                "correct": False,
                "points": 0,
                "explanation": "This is a billing/quota issue, not a technical support issue. Your health check confirmed TCC service is operational. Billing issues are handled by account management, not technical support."
            }
        }

    def start_investigation(self):
        """Start the complete enhanced investigation experience with Investigation-First Flow"""
        self.clear_screen()
        self.print_banner()
        
        # Phase 1: Customer Analysis (NO QUIZ - just read ticket and documents)
        self.customer_analysis_phase()
        
        # Phase 2: Investigation Toolbox Preview
        self.investigation_preview_phase()
        
        # Phase 3: Active Investigation with Real Commands
        self.active_investigation_phase()
        
        # Phase 4: Assessment Quiz (AFTER investigation)
        self.assessment_quiz_phase()
        
        # Phase 5: Enhanced Solution Proposal
        self.enhanced_solution_phase()

    def print_banner(self):
        """Print the investigation banner"""
        print("🕵️‍♂️ Welcome to The Quota Mystery - Complete Enhanced TSE Investigation")
        print("=" * 75)
        print()
        print("🎯 Mission: Solve a customer's TCC CI/CD failure")
        print("📊 Score: {}/{}".format(self.score, self.max_score))
        print("🔍 Essential Clues: {}/{}".format(len(self.clues_found), self.max_clues))
        print()

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')

    def customer_analysis_phase(self):
        """Phase 1: Customer Analysis - Read ticket and explore documents (NO QUIZ)"""
        print("📋 PHASE 1: CUSTOMER ANALYSIS")
        print("=" * 35)
        print()
        
        # Show customer ticket
        print("📞 CUSTOMER TICKET:")
        print("-" * 20)
        print(self.customer_ticket)
        print()
        
        input("⏎ Press Enter to view supporting documents...")
        print()
        
        # Show supporting documents
        self.show_supporting_documents()
        
        # Optional document exploration
        self.allow_document_exploration()
        
        print()
        print("🎯 Ready to investigate? You'll form your hypothesis AFTER gathering evidence!")
        input("⏎ Press Enter to proceed to Investigation Toolbox...")

    def show_supporting_documents(self):
        """Show supporting documents with key insights"""
        print("📁 SUPPORTING DOCUMENTS AVAILABLE:")
        print("=" * 40)
        
        for i, doc in enumerate(self.supporting_documents, 1):
            print(f"\n📄 {i}. {doc['name']}")
            print(f"   📍 File: {doc['file']}")
            print(f"   💡 Key Insight: {doc['key_insight']}")
            print(f"   📋 Preview:")
            for line in doc['preview'].split('\n')[:3]:
                print(f"      {line}")
            if len(doc['preview'].split('\n')) > 3:
                remaining_lines = len(doc['preview'].split('\n')) - 3
                print(f"      ... ({remaining_lines} more lines)")
        
        print()

    def allow_document_exploration(self):
        """Allow TSE to explore specific documents"""
        while True:
            explore = input("🔍 Would you like to explore any specific document? (1-4, or 'skip'): ").strip()
            
            if explore.lower() == 'skip':
                break
            elif explore.isdigit() and 1 <= int(explore) <= len(self.supporting_documents):
                doc = self.supporting_documents[int(explore) - 1]
                print(f"\n📄 {doc['name']} - Full Content:")
                print("-" * 40)
                print(doc['preview'])
                print()
                print(f"💡 Key Insight: {doc['key_insight']}")
                print()
            else:
                print("❌ Please enter 1-4 or 'skip'")

    def take_assessment_quiz(self):
        """Take the enhanced assessment quiz with randomized options and multiple attempts"""
        print("🧠 ASSESSMENT QUIZ:")
        print("-" * 25)
        print(self.analysis_quiz["question"])
        print()
        
        # Randomize the quiz options to mix correct and incorrect answers
        import random
        options_list = list(self.analysis_quiz["options"].items())
        random.shuffle(options_list)
        
        # Create randomized option mapping
        randomized_options = {}
        option_letters = ['A', 'B', 'C', 'D', 'E']
        
        for i, (original_key, data) in enumerate(options_list):
            randomized_options[option_letters[i]] = data
            print(f"{option_letters[i]}. {data['text']}")
        
        print()
        
        while self.quiz_attempts < self.max_quiz_attempts:
            self.quiz_attempts += 1
            remaining = self.max_quiz_attempts - self.quiz_attempts
            
            if remaining > 0:
                print(f"🎯 Attempt {self.quiz_attempts} of {self.max_quiz_attempts} (remaining: {remaining})")
            else:
                print(f"🎯 Final attempt ({self.quiz_attempts} of {self.max_quiz_attempts})")
            
            choice = input("Enter your hypothesis (A-E): ").strip().upper()
            
            if choice in randomized_options:
                selected = randomized_options[choice]
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
                if remaining > 0:
                    print(f"🔄 You have {remaining} attempts remaining.")
                else:
                    print("🎯 This was your final attempt.")
        
        print()
        input("⏎ Press Enter to proceed to Solution Proposal...")

    def investigation_preview_phase(self):
        """Phase 2: Investigation Toolbox Preview with Randomized Order"""
        self.clear_screen()
        print("🔧 PHASE 2: INVESTIGATION TOOLBOX")
        print("=" * 35)
        print()
        print("Here are your diagnostic tools. You'll run the actual commands")
        print("and see real outputs. Plan your investigation strategy!")
        print()
        
        # Randomize tool order for more realistic investigation
        import random
        essential_tools = ["1", "2", "3", "4", "5", "6"]
        exploratory_tools = ["7", "8", "9", "10"]
        
        # Shuffle the order to confuse TSEs a little
        random.shuffle(essential_tools)
        random.shuffle(exploratory_tools)
        
        print("🎯 ESSENTIAL TOOLS (Complete All 6 - Order Randomized):")
        print("-" * 55)
        for i, tool_id in enumerate(essential_tools, 1):
            tool = self.investigation_tools[tool_id]
            print(f"{i}. 🔍 {tool['name']}")
            print(f"   💭 {tool['description']}")
            print(f"   💻 Command: {tool['command']}")
            print(f"   🎯 Points: {tool['points']}")
            print()
        
        print("🎭 EXPLORATORY TOOLS (Optional, No Penalty - Order Randomized):")
        print("-" * 60)
        for i, tool_id in enumerate(exploratory_tools, 7):
            tool = self.investigation_tools[tool_id]
            print(f"{i}. 🔍 {tool['name']}")
            print(f"   💭 {tool['description']}")
            print(f"   💻 Command: {tool['command']}")
            print(f"   🎯 Points: 0 (exploratory)")
            print()
        
        print("🎯 INVESTIGATION STRATEGY:")
        print("-" * 25)
        print("• Essential tools will reveal the root cause - complete all 6")
        print("• Exploratory tools are optional - won't hurt your score")
        print("• Run tools in any order you prefer")
        print("• Focus on gathering evidence systematically")
        print("• Use 'customer' command to re-read ticket anytime")
        print()
        
        input("⏎ Press Enter to start active investigation...")

    def active_investigation_phase(self):
        """Phase 3: Active Investigation with Real Command Execution"""
        self.clear_screen()
        print("🕵️‍♂️ PHASE 3: ACTIVE INVESTIGATION")
        print("=" * 35)
        print()
        print("Now it's time to investigate! Run the diagnostic tools in any")
        print("order you prefer. You can always go back to review information.")
        print()
        
        while len([c for c in self.clues_found if self.investigation_tools[c]['is_essential']]) < 6:
            self.show_investigation_menu()
            
            choice = input(f"\n🎯 What would you like to investigate? (1-10, 'help', 'status', 'customer', 'toolbox', 'evidence', 'solve', 'exit'): ").strip().lower()
            
            if choice == 'help':
                self.show_help()
            elif choice == 'status':
                self.show_status()
            elif choice == 'customer':
                self.show_customer_info()
            elif choice == 'toolbox':
                self.show_toolbox()
            elif choice == 'evidence':
                self.show_evidence_summary()
            elif choice == 'solve':
                if self.allow_early_solve():
                    return  # Move to solution phase
            elif choice == 'exit':
                if self.confirm_exit():
                    return
            elif choice.isdigit() and 1 <= int(choice) <= 10:
                tool_id = choice
                if tool_id not in self.clues_found:
                    self.execute_investigation_tool(tool_id)
                else:
                    print("ℹ️  You've already investigated this tool!")
            else:
                print("❌ Invalid choice. Try again.")
            
            input("\n⏎ Press Enter to continue...")

    def show_investigation_menu(self):
        """Show the investigation menu with randomized tool order"""
        print("\n🔍 INVESTIGATION TOOLS (Order Randomized):")
        print("-" * 40)
        
        essential_completed = len([c for c in self.clues_found if self.investigation_tools[c]['is_essential']])
        
        # Randomize the tool order for each menu display
        import random
        tool_ids = list(self.investigation_tools.keys())
        random.shuffle(tool_ids)
        
        for tool_id in tool_ids:
            tool = self.investigation_tools[tool_id]
            status = "✅" if tool_id in self.clues_found else "🔍"
            essential_indicator = "🎯" if tool['is_essential'] else "🎭"
            print(f"{tool_id}. {status} {essential_indicator} {tool['name']}")
            print(f"   💭 {tool['description']}")
        
        print(f"\n📊 INVESTIGATION STATUS:")
        print(f"   Score: {self.score}/{self.max_score}")
        print(f"   Essential Tools: {essential_completed}/6")
        print(f"   Progress: {essential_completed/6*100:.0f}%")

    def execute_investigation_tool(self, tool_id):
        """Execute an investigation tool with real command execution"""
        tool = self.investigation_tools[tool_id]
        
        print(f"\n🔍 {tool['name']}")
        print("=" * 50)
        print(f"💭 {tool['description']}")
        print()
        
        print("🛠️  Command to run:")
        print(f"   {tool['command']}")
        print()
        
        # TSE runs the command first
        run_it = input("🤔 Do you want to run this command? (y/n): ").strip().lower()
        
        if run_it == 'y':
            print(f"\n⚡ Executing: {tool['command']}")
            print("📋 Running command...")
            print("-" * 30)
            
            # Actually execute the command
            result = os.system(tool['command'])
            print("-" * 30)
            print("📋 Command completed!")
            print()
            
            # Show analysis
            self.show_analysis_and_clue(tool, tool_id)
        else:
            print("⏭️  Skipped this investigation step.")

    def show_analysis_and_clue(self, tool, tool_id):
        """Show analysis and clue after command execution"""
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

    def check_essential_completion(self):
        """Check if all essential tools are completed"""
        essential_completed = len([c for c in self.clues_found if self.investigation_tools[c]['is_essential']])
        
        if essential_completed == 6:
            print("🎉 ALL ESSENTIAL TOOLS COMPLETED!")
            print("✅ You've gathered all the critical evidence!")
            print("🎯 Ready to propose solutions!")
            return True
        else:
            remaining = 6 - essential_completed
            print(f"🔍 Still need {remaining} essential tools to complete investigation")
            return False

    def allow_early_solve(self):
        """Allow early solving with warnings and confirmation"""
        essential_completed = len([c for c in self.clues_found if self.investigation_tools[c]['is_essential']])
        
        if essential_completed == 6:
            print("✅ You've completed all essential tools!")
            return True
        elif essential_completed >= 3:
            # Allow early solving with warning
            print()
            print("⚠️  EARLY SOLVE WARNING:")
            print(f"   You've only gathered {essential_completed}/6 essential evidence items.")
            print("   You may miss important insights!")
            print()
            print(f"   📊 Current score: {self.score}/{self.max_score}")
            print(f"   🎯 Potential bonus: {(6-essential_completed)*15} points available from remaining tools")
            print()
            confirm = input("🤔 Are you confident you've found the root cause? (yes/no): ").strip().lower()
            
            if confirm in ['yes', 'y']:
                print()
                print("✅ Proceeding to solution phase with current evidence...")
                print("💡 Your solution evaluation will reference the evidence you gathered.")
                return True
            else:
                print()
                print("✅ Good call! Continue gathering evidence for a stronger case.")
                return False
        else:
            # Need minimum 3 essential tools
            print()
            print(f"🔍 Minimum evidence required: You need at least 3 essential tools.")
            print(f"   Current progress: {essential_completed}/3 minimum (6 recommended)")
            print("   Continue investigating to gather more evidence!")
            return False

    def show_evidence_summary(self):
        """Show summary of all evidence gathered so far"""
        print()
        print("📋 EVIDENCE SUMMARY:")
        print("=" * 50)
        
        if not self.clues_found:
            print("❌ No evidence gathered yet. Start investigating!")
            return
        
        essential_evidence = [c for c in self.clues_found if self.investigation_tools[c]['is_essential']]
        exploratory_evidence = [c for c in self.clues_found if not self.investigation_tools[c]['is_essential']]
        
        print(f"\n🎯 ESSENTIAL EVIDENCE ({len(essential_evidence)}/6):")
        print("-" * 50)
        for clue_id in essential_evidence:
            tool = self.investigation_tools[clue_id]
            print(f"\n✅ {tool['name']}")
            print(f"   💡 Key Finding: {tool['analysis_tip']}")
        
        if exploratory_evidence:
            print(f"\n🎭 EXPLORATORY EVIDENCE ({len(exploratory_evidence)}/4):")
            print("-" * 50)
            for clue_id in exploratory_evidence:
                tool = self.investigation_tools[clue_id]
                print(f"\n✅ {tool['name']}")
                print(f"   💡 Finding: {tool['analysis_tip']}")
        
        print(f"\n📊 EVIDENCE ANALYSIS:")
        print(f"   Total Evidence Items: {len(self.clues_found)}/10")
        print(f"   Essential Tools Completed: {len(essential_evidence)}/6")
        print(f"   Current Score: {self.score}/{self.max_score}")
        
        if len(essential_evidence) >= 3:
            print(f"   ✅ Sufficient evidence to propose solution (minimum 3/6 reached)")
        else:
            print(f"   ⚠️  Need {3-len(essential_evidence)} more essential tools to propose solution")
        
        print()

    def confirm_exit(self):
        """Confirm exit and handle cleanup"""
        print()
        print("🚪 EXIT CONFIRMATION:")
        print("-" * 25)
        print("Are you sure you want to exit the lab?")
        print("⚠️  Progress will not be saved.")
        print()
        
        confirm = input("Exit lab? (yes/no): ").strip().lower()
        
        if confirm in ['yes', 'y']:
            print()
            print("👋 Thank you for using the TCC Lab!")
            print("   Feel free to run the lab again anytime.")
            print()
            import sys
            sys.exit(0)
        else:
            print()
            print("✅ Continuing investigation...")
            return False

    def assessment_quiz_phase(self):
        """Phase 4: Assessment Quiz (AFTER investigation) with exit option"""
        self.clear_screen()
        self.print_banner()
        print("🧠 PHASE 4: ASSESSMENT QUIZ")
        print("=" * 35)
        print()
        print("Now that you've gathered evidence through investigation,")
        print("let's test your understanding of the root cause!")
        print()
        print("💡 Type 'evidence' to review your findings, or 'exit' to leave the lab")
        print()
        
        # Take assessment quiz
        self.take_assessment_quiz()
        
        print()
        choice = input("⏎ Press Enter to proceed to Solution Proposal (or 'exit' to leave): ").strip().lower()
        if choice == 'exit':
            self.confirm_exit()

    def enhanced_solution_phase(self):
        """Phase 5: Enhanced Solution Proposal with Evidence-Based Evaluation"""
        self.clear_screen()
        print("🎯 PHASE 5: ENHANCED SOLUTION PROPOSAL")
        print("=" * 45)
        print()
        print("Based on your investigation findings, propose solutions to the customer.")
        print()
        print("💡 Type 'evidence' to review your findings before proposing solutions")
        print()
        print("🎯 SOLUTION GUIDANCE:")
        print("• Choose solutions that address the ROOT CAUSE")
        print("• Select multiple solutions for comprehensive approach")
        print("• Focus on solutions with strong evidence support")
        print("• Consider both immediate and long-term fixes")
        print()
        print("📊 EVALUATION CRITERIA:")
        print("• Correctness of the solution")
        print("• Evidence you've gathered")
        print("• Alignment with root cause")
        print("• Professional customer communication")
        print()
        
        # Show solutions with evidence indicators and guidance
        print("🎯 AVAILABLE SOLUTIONS:")
        print("-" * 25)
        for sol_id, solution in self.solutions.items():
            evidence_status = "✅" if all(clue in self.clues_found for clue in solution.get("evidence_required", [])) else "⚠️"
            evidence_count = len([c for c in solution.get("evidence_required", []) if c in self.clues_found])
            evidence_total = len(solution.get("evidence_required", []))
            
            print(f"{sol_id}. {evidence_status} {solution['title']}")
            print(f"   💭 {solution['description']}")
            if solution.get("evidence_required"):
                print(f"   🔍 Evidence: {evidence_count}/{evidence_total} gathered")
            print()
        
        print("💡 TIP: Choose solutions 1, 2, and 3 for maximum points!")
        print("   These address the root cause with strong evidence.")
        print()
        
        chosen_solutions = []
        while True:
            choice_input = input("🎯 Enter solution numbers (e.g., '1 2 3'), 'evidence' to review, 'exit' to leave, or 'done' to finish: ").strip().lower()
            
            if choice_input == 'done':
                break
            elif choice_input == 'evidence':
                self.show_evidence_summary()
                continue
            elif choice_input == 'exit':
                if self.confirm_exit():
                    return
                continue
            
            try:
                choices = [c.strip() for c in choice_input.split()]
                for c in choices:
                    if c in self.solutions and c not in chosen_solutions:
                        chosen_solutions.append(c)
                        self.evaluate_solution(c)
                    elif c not in self.solutions:
                        print(f"❌ Invalid solution number: {c}")
            except:
                print("❌ Invalid input. Please enter numbers, 'evidence', 'exit', or 'done'.")
        
        # Final summary
        self.show_solution_summary(chosen_solutions)

    def evaluate_solution(self, solution_id):
        """Evaluate a solution with detailed feedback referencing gathered evidence"""
        solution = self.solutions[solution_id]
        
        print(f"\n🎯 EVALUATING: {solution['title']}")
        print("=" * 50)
        
        if solution["correct"]:
            # Check if TSE has required evidence
            required_evidence = solution.get("evidence_required", [])
            gathered_required = [clue for clue in required_evidence if clue in self.clues_found]
            has_all_evidence = len(gathered_required) == len(required_evidence)
            
            if has_all_evidence:
                self.score += solution['points']
                print("✅ EXCELLENT SOLUTION!")
                print("📊 Evidence-based reasoning:")
                print(f"   {solution['explanation']}")
                print(f"📈 Points earned: {solution['points']}")
                
                # Show specific evidence gathered
                if gathered_required:
                    print("\n🔍 Evidence from your investigation:")
                    for clue_id in gathered_required:
                        tool = self.investigation_tools[clue_id]
                        print(f"   ✅ Tool {clue_id}: {tool['name']}")
                        print(f"      Finding: {tool['analysis_tip']}")
            else:
                # Partial points for correct solution but missing evidence
                partial_points = solution['points'] // 2
                self.score += partial_points
                print("⚠️  GOOD SOLUTION, but missing some evidence:")
                print(f"   {solution['explanation']}")
                print(f"📈 Points earned: {partial_points} (reduced for incomplete evidence)")
                
                if gathered_required:
                    print("\n✅ Evidence you gathered:")
                    for clue_id in gathered_required:
                        tool = self.investigation_tools[clue_id]
                        print(f"   • Tool {clue_id}: {tool['name']}")
                
                missing = [clue for clue in required_evidence if clue not in self.clues_found]
                if missing:
                    print("\n⚠️  Missing evidence (would strengthen your case):")
                    for clue_id in missing:
                        tool = self.investigation_tools[clue_id]
                        print(f"   • Tool {clue_id}: {tool['name']}")
        else:
            print("❌ INCORRECT SOLUTION")
            print("📚 Why this won't work:")
            print(f"   {solution['explanation']}")
            print("📈 Points earned: 0")
            
            # Show what evidence they actually gathered
            if self.clues_found:
                print("\n💡 Review your evidence:")
                print("   Type 'evidence' to see what you discovered")
                print("   Focus on solutions that match your findings")

    def show_solution_summary(self, chosen_solutions):
        """Show comprehensive final solution summary with detailed feedback"""
        print("\n🎉 INVESTIGATION COMPLETE!")
        print("=" * 30)
        print(f"📊 Final Score: {self.score}/{self.max_score}")
        
        essential_completed = len([c for c in self.clues_found if self.investigation_tools[c]['is_essential']])
        print(f"🔍 Essential Tools Used: {essential_completed}/6")
        
        correct_solutions = [s for s in chosen_solutions if self.solutions[s]["correct"]]
        incorrect_solutions = [s for s in chosen_solutions if not self.solutions[s]["correct"]]
        
        print(f"✅ Correct Solutions: {len(correct_solutions)}")
        print(f"❌ Incorrect Solutions: {len(incorrect_solutions)}")
        
        # Comprehensive feedback
        print("\n📋 COMPREHENSIVE FEEDBACK:")
        print("-" * 30)
        
        if len(correct_solutions) >= 3:
            print("🎯 EXCELLENT! You chose the optimal solutions!")
            print("   You addressed the root cause comprehensively.")
        elif len(correct_solutions) >= 2:
            print("✅ GOOD! You identified key solutions.")
            print("   Consider adding more solutions for comprehensive coverage.")
        elif len(correct_solutions) >= 1:
            print("⚠️  PARTIAL! You found some correct solutions.")
            print("   Review the root cause to identify additional solutions.")
        else:
            print("❌ NEEDS IMPROVEMENT! No correct solutions chosen.")
            print("   Focus on solutions that address quota exhaustion.")
        
        if incorrect_solutions:
            print(f"\n🔍 INCORRECT SOLUTIONS ANALYSIS:")
            for sol_id in incorrect_solutions:
                solution = self.solutions[sol_id]
                print(f"   • {solution['title']}: {solution['explanation']}")
        
        # Professional customer response
        print("\n💼 PROFESSIONAL CUSTOMER RESPONSE:")
        print("-" * 40)
        print("Based on your investigation findings:")
        print("• Root Cause: TCC quota exceeded (52/50 minutes used)")
        print("• Evidence: Account usage data, execution logs, billing model")
        print("• Timeline: Issue started when quota was exhausted 48 hours ago")
        print("• Local vs CI: Local tests don't count against quota")
        print()
        print("Recommended Solutions:")
        for sol_id in correct_solutions:
            solution = self.solutions[sol_id]
            print(f"• {solution['title']}: {solution['description']}")
        
        print("\n🎯 Congratulations! You've successfully solved The Quota Mystery!")
        print("   This experience has built your TSE investigation skills!")

    def show_help(self):
        """Show help information"""
        print("\n📚 INVESTIGATION HELP:")
        print("-" * 40)
        print("🎯 Goal: Find why CI fails but local works")
        print("🔍 Method: Use diagnostic tools to gather evidence")
        print()
        print("📋 AVAILABLE COMMANDS:")
        print("  1-10     - Run investigation tool")
        print("  help     - Show this help message")
        print("  status   - Show investigation progress")
        print("  customer - Review customer ticket")
        print("  toolbox  - Review investigation tools")
        print("  evidence - Show evidence summary (NEW!)")
        print("  solve    - Propose solution (min 3/6 tools)")
        print("  exit     - Exit the lab")
        print()
        print("📊 SCORING:")
        print("  🎯 Essential tools: Give points for evidence")
        print("  🎭 Exploratory tools: No points, optional")
        print()
        print("💡 TIPS:")
        print("  • Minimum 3 essential tools to solve (6 recommended)")
        print("  • Use 'evidence' to review what you've found")
        print("  • Early solving possible but may miss insights")
        print("  • You can exit anytime with 'exit' command")

    def show_status(self):
        """Show current investigation status"""
        essential_completed = len([c for c in self.clues_found if self.investigation_tools[c]['is_essential']])
        
        print(f"\n📊 INVESTIGATION STATUS:")
        print(f"   Score: {self.score}/{self.max_score}")
        print(f"   Essential Tools: {essential_completed}/6")
        print(f"   Root Cause: {'✅ Found' if '4' in self.clues_found else '🔍 Still investigating'}")
        
        if self.clues_found:
            print(f"\n🔍 Tools Used:")
            for clue in self.clues_found:
                tool = self.investigation_tools[clue]
                essential_indicator = "🎯" if tool['is_essential'] else "🎭"
                print(f"   ✅ {essential_indicator} {tool['name']}")

    def show_customer_info(self):
        """Show customer information"""
        print("\n📞 CUSTOMER INFORMATION:")
        print("-" * 25)
        print(self.customer_ticket)
        print()
        self.show_supporting_documents()

    def show_toolbox(self):
        """Show investigation toolbox"""
        print("\n🔧 INVESTIGATION TOOLBOX:")
        print("-" * 25)
        
        print("🎯 ESSENTIAL TOOLS:")
        for tool_id in ["1", "2", "3", "4", "5", "6"]:
            tool = self.investigation_tools[tool_id]
            status = "✅ Used" if tool_id in self.clues_found else "🔍 Available"
            print(f"{tool_id}. {status} {tool['name']}")
            print(f"   💻 {tool['command']}")
        
        print("\n🎭 EXPLORATORY TOOLS:")
        for tool_id in ["7", "8", "9", "10"]:
            tool = self.investigation_tools[tool_id]
            status = "✅ Used" if tool_id in self.clues_found else "🔍 Available"
            print(f"{tool_id}. {status} {tool['name']}")
            print(f"   💻 {tool['command']}")

def main():
    """Main function to start the complete enhanced investigation"""
    engine = CompleteEnhancedInvestigationEngine()
    engine.start_investigation()

if __name__ == "__main__":
    main()