"""
Main Execution Script

Author: Youssef Amin

This script initializes the PlannerAgent and generates subgoals for a sample task.
Used to test the output of the planner before integrating with ExecutorAgent.
"""

from utils.mock_env import MockEnv
from agents.executor_agent import ExecutorAgent
from agents.planner_agent import PlannerAgent
from agents.verifier_agent import VerifierAgent
import json

def main():
    env = MockEnv()
    planner = PlannerAgent()
    executor = ExecutorAgent(env)
    verifier = VerifierAgent()

    subgoals = planner.plan("Turn Wi-Fi on and off")

    for goal in subgoals:
        print(f"\n=== Executing Subgoal: {goal} ===")
        executor.execute(goal)
        
        #get new UI after action
         ## when andopidenv is implemented: obs, _, _, _ = env.step({})
        obs = env.step({})
        ui_tree = json.loads(obs["ui_tree"])
        
        result = verifier.verify(goal, ui_tree)
        print(f"[VerifierAgent] Subgoal {'PASSED' if result else 'FAILED'}")

if __name__ == "__main__":
    main()

