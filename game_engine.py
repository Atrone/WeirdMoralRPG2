import random
from dataclasses import dataclass
from typing import List, Dict, Optional
from scenarios import base_scenarios
from metrics import MoralityTracker

@dataclass
class GameState:
    current_scene: str
    inventory: List[str]
    moral_score: int
    capability_score: int
    turns_taken: int
    weirdness_level: int

class GameEngine:
    def __init__(self, weirdness_level: int = 0):
        self.weirdness_level = weirdness_level
        self.state = GameState(
            current_scene="start",
            inventory=[],
            moral_score=0,
            capability_score=0,
            turns_taken=0,
            weirdness_level=weirdness_level
        )
        self.morality_tracker = MoralityTracker()
        self.scenarios = base_scenarios

    def get_current_scenario(self) -> Dict:
        """Get the current scenario with applied weirdness modifications"""
        base_scenario = self.scenarios[self.state.current_scene]
        modified_scenario = self._apply_weirdness(base_scenario)
        return modified_scenario

    def _apply_weirdness(self, scenario: Dict) -> Dict:
        """Apply weirdness modifications to scenario text and options"""
        if self.weirdness_level == 0:
            return scenario

        modified = scenario.copy()
        # Modify description based on weirdness level
        weird_adjectives = ["strange", "bizarre", "otherworldly", "incomprehensible"]
        weird_factor = self.weirdness_level / 100
        
        desc = modified["description"]
        for adj in weird_adjectives:
            if random.random() < weird_factor:
                desc = desc.replace("the", f"the {adj}")
        
        modified["description"] = desc
        return modified

    def make_choice(self, choice_index: int) -> tuple[str, int, int]:
        """Process a player's choice and return (result_text, moral_score_delta, capability_score_delta)"""
        scenario = self.get_current_scenario()
        choice = scenario["choices"][choice_index]
        
        # Update scores
        moral_delta = choice.get("moral_value", 0)
        capability_delta = choice.get("capability_value", 0)
        
        self.state.moral_score += moral_delta
        self.state.capability_score += capability_delta
        self.state.turns_taken += 1
        
        # Track choice morality
        self.morality_tracker.record_choice(
            choice["text"],
            moral_delta,
            self.weirdness_level
        )
        
        # Update game state
        self.state.current_scene = choice.get("next_scene", "end")
        
        return choice["result"], moral_delta, capability_delta

    def is_game_over(self) -> bool:
        """Check if the game has ended"""
        return self.state.current_scene == "end" or self.state.turns_taken >= MAX_TURNS

    def get_final_scores(self) -> Dict:
        """Return final game scores"""
        return {
            "moral_score": self.state.moral_score,
            "capability_score": self.state.capability_score,
            "turns_taken": self.state.turns_taken,
            "weirdness_level": self.weirdness_level
        }
