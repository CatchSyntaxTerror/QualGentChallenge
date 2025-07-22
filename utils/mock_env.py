"""
Mock Environment

Author: Youssef Amin

This class is a mock envirment for testing scrpit logic
"""
import json
import numpy as np


class MockEnv:
    def __init__(self):
        self.step_count = 0
        self.wifi_on = True

    def reset(self):
        print("[MockEnv] Resetting environment")
        return self._get_mock_obs()

    def step(self, action, subgoal=None):
        if action:
            print(f"[MockEnv] Step {self.step_count}: Action received → {action}")
        else:
            print(f"[MockEnv] Step {self.step_count}: No action, just observing")
            
        # toggle wifi state
        if subgoal and "toggle wi-fi" in subgoal.lower():
            self.wifi_on = not self.wifi_on
            print(f"[MockEnv] Wi-Fi toggled → {'ON' if self.wifi_on else 'OFF'}")
    
        self.step_count += 1
        
        return {
            "ui_tree": json.dumps(self._build_ui_tree())
        }

    def _get_mock_obs(self):
        return {
            "ui_tree": json.dumps(self._build_ui_tree())
        }

    def render(self, mode='rgb_array'):
        print("[MockEnv] Render called")
        return np.zeros((480, 720, 3), dtype=np.uint8)  
    
    def _build_ui_tree(self):
        return {
            "class": "android.widget.FrameLayout",
            "children": [
                {
                    "class": "android.widget.TextView",
                    "text": "Network & Internet",
                    "bounds": [[100, 200], [400, 300]]
                },
                {
                    "class": "android.widget.TextView",
                    "text": "Wi-Fi",
                    "state": "on" if self.wifi_on else "off",
                    "bounds": [[100, 400], [400, 500]]
                },
                {
                    "class": "android.widget.TextView",
                    "text": "Settings",
                    "bounds": [[100, 100], [400, 180]]
                }
            ]
        }

