"""
Executor Agent

Author: Youssef Amin

This module defines the ExecutorAgent class, responsible for mapping subgoals
into touch or keyboard actions and executing them through the AndroidEnv API.
"""

import json
import re
import time
from PIL import Image
import os
import numpy as np

class ExecutorAgent:
    def __init__(self, env):
        """
        Initializes the ExecutorAgent with a given AndroidEnv environment.
        """
        self.env = env
        self.screenshot_count = 0

    def execute(self, subgoal: str):
        """
        Executes the given subgoal using the AndroidEnv.

        Args:
            subgoal (str): User instruction, e.g. "Tap on 'Wi-Fi'"
        """
        print(f"[ExecutorAgent] Executing: {subgoal}")
        
        # observe current UI state
        ## when andopidenv is implemented: obs, _, _, _  = self.env.step({})
        obs = self.env.step({}) 
        ui_tree = json.loads(obs["ui_tree"])
        
        match = re.search(r"wait for (\d+) second", subgoal.lower())
        if match:
            duration = int(match.group(1))
            print(f"[ExecutorAgent] Waiting {duration} second(s)...")
            time.sleep(duration)
            return
        
        # find node that matches sub goal
        target_text = self.extract_target_text(subgoal)
        if not target_text:
            print("[ExecutorAgent] Could not extract target from subgoal.")
            return
        
        # extract target for actionable subgoals
        element = self.find_ui_element(ui_tree, target_text)
        if element:
            x, y = self.get_center_coordinates(element["bounds"])
            print(f"[ExecutorAgent] Tapping ({x}, {y}) on '{target_text}'")
            action = {
                "touch": {
                    "x": x,
                    "y": y,
                    "action_type": "down_up"
                }
            }
            self.env.step(action, subgoal=subgoal)
            
            # Save a screenshot to logs
            #chnage logs/mock to log/android when your done with the mock test
            
            frame = self.env.render(mode="rgb_array")
            log_dir = "logs/mock" 
            os.makedirs(log_dir, exist_ok=True)
            self.screenshot_count += 1
            filename = f"logs/mock/step_{self.screenshot_count}.png"
            Image.fromarray(frame).save(filename)
            print(f"[ExecutorAgent] Saved screenshot → {filename}")
        else:
            print(f"[ExecutorAgent] Element '{target_text}' not found in UI.")

    # TODO: Refactor this to use a smarter matching function
    def extract_target_text(self, subgoal: str):
        subgoal = subgoal.lower()
        if "wi-fi" in subgoal:
            return "Wi-Fi"
        if "network & internet" in subgoal:
            return "Network & Internet"
        if "settings" in subgoal:
            return "Settings"
        return None

    def find_ui_element(self, node, target_text):
        """
        Recursively search the UI tree for a node with matching text.
        """
        if isinstance(node, dict):
            if node.get("text") == target_text:
                return node
            for child in node.get("children", []):
                result = self.find_ui_element(child, target_text)
                if result:
                    return result
        return None

    def get_center_coordinates(self, bounds: list):
        """
        Calculates center (x, y) from bounds [[x1, y1], [x2, y2]]
        """
        x1, y1 = bounds[0]
        x2, y2 = bounds[1]
        return (x1 + x2) // 2, (y1 + y2) // 2
