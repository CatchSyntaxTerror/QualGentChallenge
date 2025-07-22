"""
Main Execution Script

Author: Youssef Amin

This script initializes the PlannerAgent and generates subgoals for a sample task.
Used to test the output of the planner before integrating with ExecutorAgent.
"""

from agents.planner_agent import PlannerAgent

if __name__ == "__main__":
    planner = PlannerAgent()
    steps = planner.plan("Turn Wi-Fi on and off")

    print("Generated Subgoals:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")
