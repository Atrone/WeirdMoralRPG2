import random
from typing import Dict, List

class WeirdnessGenerator:
    def __init__(self):
        self.weird_adjectives = [
            "otherworldly", "bizarre", "peculiar", "surreal", "uncanny",
            "ethereal", "metaphysical", "anomalous", "paradoxical"
        ]
        self.weird_objects = [
            "crystal", "portal", "dimension", "reality", "consciousness",
            "entity", "phenomenon", "manifestation", "construct"
        ]

    def modify_text(self, text: str, weirdness_level: int) -> str:
        """Modify text based on weirdness level"""
        if weirdness_level < 5:
            return text
            
        weird_factor = weirdness_level / 100
        words = text.split()
        
        for i in range(len(words)):
            if random.random() < weird_factor:
                if words[i] in ["the", "a", "an"]:
                    words[i] = f"{words[i]} {random.choice(self.weird_adjectives)}"
                elif words[i] in ["person", "place", "thing"]:
                    words[i] = random.choice(self.weird_objects)
                    
        return " ".join(words)

    def generate_weird_scenario(self, base_scenario: Dict, weirdness_level: int) -> Dict:
        """Generate a weird version of a scenario"""
        modified = base_scenario.copy()
        modified["description"] = self.modify_text(base_scenario["description"], weirdness_level)
        
        modified_choices = []
        for choice in base_scenario["choices"]:
            weird_choice = choice.copy()
            weird_choice["text"] = self.modify_text(choice["text"], weirdness_level)
            weird_choice["result"] = self.modify_text(choice["result"], weirdness_level)
            modified_choices.append(weird_choice)
            
        modified["choices"] = modified_choices
        return modified
