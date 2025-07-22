"""
Planner Agent

Author: Youssef Amin

This module defines the PlannerAgent class, which takes QA task prompts
and turns them into a sequence of subgoals for Android UI testing.

Currently supports: "Turn Wi-Fi on and off"
"""
class PlannerAgent:
    def __init__(self):
        self.goal = None

    def plan(self, goal_prompt: str):
        """
        Turns a natural language QA goal into subgoals

        Args:
            goal_prompt (str): The input command string

        Returns:
            List[str]: A list of subgoals.
        """
        self.goal = goal_prompt.strip().lower()

        if "wifi" in self.goal or "wi-fi" in self.goal:
            return [
                "Launch Settings app",
                "Tap on 'Network & Internet'",
                "Tap on 'Wi-Fi'",
                "Toggle Wi-Fi OFF",
                "Wait for 2 seconds",
                "Toggle Wi-Fi ON"
            ]
        else:
            return ["[PlannerAgent] Sorry, this goal is not supported yet."]
