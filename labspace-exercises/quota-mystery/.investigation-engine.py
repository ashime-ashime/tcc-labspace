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

        # Supporting documents for customer analysis
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
                "key_insight": "🚨 Missing testcontainers-cloud-setup-action! This explains the timeout."
            },
            {
                "name": "Execution Logs",
                "file": "customer-report/github-actions-logs.txt",
                "preview": """[2025-01-09 10:15:23] Starting GitHub Actions workflow
[2025-01-09 10:15:26] Attempting Testcontainers Cloud setup...
[2025-01-09 10:17:30] ERROR: Testcontainers Cloud setup failed: Quota exceeded
[2025-01-09 10:17:30] Workflow terminated due to timeout""",
                "key_insight": "🎯 Key error: 'Quota exceeded' during TCC setup - smoking gun!"
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
                "key_insight": "📊 Legacy trial plan with quota exceeded (52/50 minutes used)"
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
                "key_insight": "📈 Visual confirmation: Quota exceeded 48 hours ago"
            }
        ]

        # Enhanced analysis quiz
        self.analysis_quiz = {
            "question": "Based on the ticket and supporting documents, what's your initial hypothesis?",
            "options": {
                "A": {
                    "text": "Authentication/Token issue",
                    "insight": "Good thinking! Token regeneration suggests auth problems, but customer already tried this.",
                    "points": 3
                },
                "B": {
                    "text": "Quota/Billing problem",
                    "insight": "🎯 EXCELLENT! The logs show 'Quota exceeded' and account shows 52/50 minutes used. This is the root cause!",
                    "points": 20
                },
                "C": {
                    "text": "Network connectivity issue",
                    "insight": "Reasonable thought, but customer already verified network connectivity.",
                    "points": 2
                },
                "D": {
                    "text": "Configuration error",
                    "insight": "Partially correct! Missing TCC setup action is a secondary issue, but not the root cause.",
                    "points": 8
                },
                "E": {
                    "text": "Service outage",
                    "insight": "Customer already checked - TCC service is operational.",
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
        """Start the complete enhanced investigation experience"""
        self.clear_screen()
        self.print_banner()
        
        # Phase 1: Enhanced Customer Analysis
        self.enhanced_customer_analysis_phase()
        
        # Phase 2: Investigation Toolbox Preview
        self.investigation_preview_phase()
        
        # Phase 3: Active Investigation with Real Commands
        self.active_investigation_phase()
        
        # Phase 4: Enhanced Solution Proposal
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

    def enhanced_customer_analysis_phase(self):
        """Phase 1: Enhanced Customer Analysis with Supporting Documents"""
        print("📋 PHASE 1: ENHANCED CUSTOMER ANALYSIS")
        print("=" * 45)
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
        
        # Assessment quiz
        self.take_assessment_quiz()

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
        """Take the enhanced assessment quiz"""
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
        print("Here are your diagnostic tools. You'll run the actual commands")
        print("and see real outputs. Plan your investigation strategy!")
        print()
        
        print("🎯 ESSENTIAL TOOLS (Complete All 6):")
        print("-" * 35)
        for tool_id in ["1", "2", "3", "4", "5", "6"]:
            tool = self.investigation_tools[tool_id]
            print(f"{tool_id}. 🔍 {tool['name']}")
            print(f"   💭 {tool['description']}")
            print(f"   💻 Command: {tool['command']}")
            print(f"   🎯 Points: {tool['points']}")
            print()
        
        print("🎭 EXPLORATORY TOOLS (Optional, No Penalty):")
        print("-" * 40)
        for tool_id in ["7", "8", "9", "10"]:
            tool = self.investigation_tools[tool_id]
            print(f"{tool_id}. 🔍 {tool['name']}")
            print(f"   💭 {tool['description']}")
            print(f"   💻 Command: {tool['command']}")
            print(f"   🎯 Points: 0 (exploratory)")
            print()
        
        print("🎯 INVESTIGATION STRATEGY:")
        print("-" * 25)
        print("• Start with tools 1-2 (workflow and logs) for initial context")
        print("• Use tool 3 (health check) to rule out service issues")
        print("• Tools 4-5 (usage/account) will reveal the root cause")
        print("• Tool 6 (static data) provides final confirmation")
        print("• Tools 7-10 are exploratory - won't hurt your score")
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
            
            choice = input(f"\n🎯 What would you like to investigate? (1-10, 'help', 'status', 'customer', 'toolbox', 'solve'): ").strip().lower()
            
            if choice == 'help':
                self.show_help()
            elif choice == 'status':
                self.show_status()
            elif choice == 'customer':
                self.show_customer_info()
            elif choice == 'toolbox':
                self.show_toolbox()
            elif choice == 'solve':
                if self.check_essential_completion():
                    return  # Move to solution phase
                else:
                    print("🔍 You need to complete all 6 essential tools before proposing solutions!")
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
        """Show the investigation menu"""
        print("\n🔍 INVESTIGATION TOOLS:")
        print("-" * 25)
        
        essential_completed = len([c for c in self.clues_found if self.investigation_tools[c]['is_essential']])
        
        for tool_id, tool in self.investigation_tools.items():
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

    def enhanced_solution_phase(self):
        """Phase 4: Enhanced Solution Proposal with Evidence-Based Evaluation"""
        self.clear_screen()
        print("🎯 PHASE 4: ENHANCED SOLUTION PROPOSAL")
        print("=" * 45)
        print()
        print("Based on your investigation findings, propose solutions to the customer.")
        print("Each solution will be evaluated based on:")
        print("• Correctness of the solution")
        print("• Evidence you've gathered")
        print("• Alignment with root cause")
        print()
        
        # Show solutions with evidence indicators
        for sol_id, solution in self.solutions.items():
            evidence_status = "✅" if all(clue in self.clues_found for clue in solution.get("evidence_required", [])) else "⚠️"
            print(f"{sol_id}. {evidence_status} {solution['title']}")
            print(f"   💭 {solution['description']}")
            if solution.get("evidence_required"):
                print(f"   🔍 Requires evidence: {', '.join(solution['evidence_required'])}")
            print()
        
        chosen_solutions = []
        while True:
            choice_input = input("🎯 Enter solution numbers (e.g., '1 2 3'), or 'done' to finish: ").strip()
            if choice_input.lower() == 'done':
                break
            try:
                choices = [c.strip() for c in choice_input.split()]
                for c in choices:
                    if c in self.solutions and c not in chosen_solutions:
                        chosen_solutions.append(c)
                        self.evaluate_solution(c)
                    elif c not in self.solutions:
                        print(f"❌ Invalid solution number: {c}")
            except:
                print("❌ Invalid input. Please enter numbers or 'done'.")
        
        # Final summary
        self.show_solution_summary(chosen_solutions)

    def evaluate_solution(self, solution_id):
        """Evaluate a solution with detailed feedback"""
        solution = self.solutions[solution_id]
        
        print(f"\n🎯 EVALUATING: {solution['title']}")
        print("=" * 50)
        
        if solution["correct"]:
            # Check if TSE has required evidence
            has_evidence = all(clue in self.clues_found for clue in solution.get("evidence_required", []))
            
            if has_evidence:
                print("✅ EXCELLENT SOLUTION!")
                print("📊 Evidence-based reasoning:")
                print(f"   {solution['explanation']}")
                print(f"📈 Points earned: {solution['points']}")
                
                # Show specific evidence
                print("\n🔍 Evidence from your investigation:")
                for clue in solution.get("evidence_required", []):
                    tool = next(t for t in self.investigation_tools.values() if t['clue'] == clue)
                    print(f"   • {tool['name']}: {tool['analysis_tip']}")
            else:
                print("⚠️  GOOD SOLUTION, but missing evidence:")
                print(f"   {solution['explanation']}")
                print(f"📈 Points earned: {solution['points']} (reduced for missing evidence)")
                print("\n🔍 Missing evidence:")
                for clue in solution.get("evidence_required", []):
                    if clue not in self.clues_found:
                        tool = next(t for t in self.investigation_tools.values() if t['clue'] == clue)
                        print(f"   • {tool['name']} - Run this tool to strengthen your solution")
        else:
            print("❌ INCORRECT SOLUTION")
            print("📚 Why this won't work:")
            print(f"   {solution['explanation']}")
            print("📈 Points earned: 0")
            print("\n💡 Better approach:")
            print("   Focus on solutions that address the root cause: quota exhaustion")

    def show_solution_summary(self, chosen_solutions):
        """Show final solution summary"""
        print("\n🎉 INVESTIGATION COMPLETE!")
        print("=" * 30)
        print(f"📊 Final Score: {self.score}/{self.max_score}")
        
        essential_completed = len([c for c in self.clues_found if self.investigation_tools[c]['is_essential']])
        print(f"🔍 Essential Tools Used: {essential_completed}/6")
        
        correct_solutions = [s for s in chosen_solutions if self.solutions[s]["correct"]]
        incorrect_solutions = [s for s in chosen_solutions if not self.solutions[s]["correct"]]
        
        print(f"✅ Correct Solutions: {len(correct_solutions)}")
        print(f"❌ Incorrect Solutions: {len(incorrect_solutions)}")
        
        print("\n💼 CUSTOMER COMMUNICATION TEMPLATE:")
        print("-" * 35)
        print("Based on your investigation findings:")
        print("• Root Cause: TCC quota exceeded (52/50 minutes used)")
        print("• Evidence: Account usage data, execution logs, billing model")
        print("• Recommended Solutions: Upgrade plan, optimize usage, local testing")
        print("• Timeline: Issue started when quota was exhausted 48 hours ago")
        print("• Local vs CI: Local tests don't count against quota")
        
        print("\n🎯 Excellent detective work! You've successfully solved The Quota Mystery!")

    def show_help(self):
        """Show help information"""
        print("\n📚 INVESTIGATION HELP:")
        print("-" * 25)
        print("🎯 Goal: Find why CI fails but local works")
        print("🔍 Method: Use diagnostic tools to gather evidence")
        print("📊 Scoring: Essential tools give points, exploratory tools don't")
        print("💡 Tips: Complete all 6 essential tools for full investigation")
        print("🔄 Freedom: Go back to customer info or toolbox anytime")

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