"""
Verifier Agent

Author: Youssef Amin

inspects the updated UI and verifies whether the expected change or element is present.
"""
import re
import json

class VerifierAgent:
    def __init__(self):
        pass

    def verify(self, subgoal: str, ui_tree: dict) -> bool:
        print(f"[VerifierAgent] Verifying: {subgoal}")

        # Handle "Wait" subgoals – nothing to verify
        if "wait" in subgoal.lower():
            print("[VerifierAgent] Nothing to verify for wait step.")
            return True

        # Handle toggle Wi-Fi
        if "toggle wi-fi" in subgoal.lower():
            expected_state = "on" if "on" in subgoal.lower() else "off"
            return self.verify_wifi_state(ui_tree, expected_state)

        # Extract quoted target text (e.g., 'Wi-Fi')
        target_text = self.extract_target_text(subgoal)
        if not target_text:
            # Fallback for "Launch Settings app" or other fuzzy matches
            if "launch settings" in subgoal.lower():
                found = self.find_text(ui_tree, "Settings")
                if found:
                    print("[VerifierAgent] Verified: Found 'Settings'")
                    return True
            print("[VerifierAgent] No target to verify.")
            return False

        # Regular verification path
        found = self.find_text(ui_tree, target_text)
        if found:
            print(f"[VerifierAgent] Verified: Found '{target_text}'")
            return True
        else:
            print(f"[VerifierAgent] Verification FAILED: '{target_text}' not found")
            return False

    def extract_target_text(self, subgoal: str) -> str | None:
        match = re.search(r"'(.*?)'", subgoal)
        if match:
            return match.group(1)
        return None

    def find_text(self, node: dict, target: str) -> bool:
        """Recursively search for the target text in the UI tree."""
        if isinstance(node, dict):
            if node.get("text", "").lower() == target.lower():
                return True
            for child in node.get("children", []):
                if self.find_text(child, target):
                    return True
        elif isinstance(node, list):
            for item in node:
                if self.find_text(item, target):
                    return True
        return False

    def verify_wifi_state(self, node: dict, expected_state: str) -> bool:
        """Look for the 'Wi-Fi' node and check its state."""
        if isinstance(node, dict):
            text = node.get("text", "").lower()
            state = node.get("state", "").lower()
            if "wi-fi" in text and state == expected_state:
                print(f"[VerifierAgent] Found Wi-Fi state: {expected_state.upper()}")
                return True
            for child in node.get("children", []):
                if self.verify_wifi_state(child, expected_state):
                    return True
        elif isinstance(node, list):
            for item in node:
                if self.verify_wifi_state(item, expected_state):
                    return True
        return False
