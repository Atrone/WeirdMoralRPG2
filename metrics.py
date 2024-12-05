from typing import List, Dict
from dataclasses import dataclass, field
import json
import csv
from datetime import datetime

@dataclass
class ChoiceRecord:
    text: str
    moral_value: int
    weirdness_level: int
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

class MoralityTracker:
    def __init__(self):
        self.choices: List[ChoiceRecord] = []

    def record_choice(self, text: str, moral_value: int, weirdness_level: int):
        """Record a choice and its moral value"""
        record = ChoiceRecord(text, moral_value, weirdness_level)
        self.choices.append(record)

    def get_morality_score(self, weirdness_level: Optional[int] = None) -> float:
        """Calculate average morality score, optionally filtered by weirdness level"""
        relevant_choices = self.choices
        if weirdness_level is not None:
            relevant_choices = [c for c in self.choices if c.weirdness_level == weirdness_level]
        
        if not relevant_choices:
            return 0.0
            
        return sum(c.moral_value for c in relevant_choices) / len(relevant_choices)

    def export_csv(self, filename: str):
        """Export choice records to CSV"""
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['text', 'moral_value', 'weirdness_level', 'timestamp'])
            writer.writeheader()
            for choice in self.choices:
                writer.writerow(choice.__dict__)

    def export_json(self, filename: str):
        """Export choice records to JSON"""
        with open(filename, 'w') as f:
            json.dump([choice.__dict__ for choice in self.choices], f, indent=2)
