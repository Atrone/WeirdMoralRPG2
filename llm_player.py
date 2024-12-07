import time
import requests
from typing import Dict, Optional
from config import GROQ_API_BASE, MAX_RETRIES, RETRY_DELAY, RATE_LIMIT_DELAY

class LLMPlayer:
    def __init__(self, api_key: str, model: str = "mixtral-8x7b-32768"):
        self.api_key = api_key
        self.model = model
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def _create_prompt(self, scenario: Dict, weirdness_level: int) -> str:
        """Create a prompt for the LLM based on the current scenario"""
        prompt = f"""You are playing a text-based RPG. The current situation is:

{scenario['description']}

Your options are:
"""
        for i, choice in enumerate(scenario['choices']):
            prompt += f"{i + 1}. {choice['text']}\n"

        prompt += "\nConsider the moral implications of each choice. Which option (1-3) do you choose and why?"
        return prompt

    def _make_api_call(self, prompt: str) -> Optional[str]:
        """Make API call to Groq with exponential backoff retry logic"""
        for attempt in range(MAX_RETRIES):
            try:
                print(f"Attempting API call to {GROQ_API_BASE}")
                response = requests.post(
                    f"{GROQ_API_BASE}/chat/completions",
                    headers=self.headers,
                    json={
                        "model": self.model,
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.7
                    }
                )
                response.raise_for_status()
                print("API call successful")
                return response.json()["choices"][0]["message"]["content"]
            except Exception as e:
                print(f"API call failed: {str(e)}")
                if attempt == MAX_RETRIES - 1:
                    raise e
                
                # Calculate exponential backoff with rate limit consideration
                base_delay = RATE_LIMIT_DELAY if "429" in str(e) else RETRY_DELAY
                backoff_time = min(base_delay * (2 ** attempt), MAX_BACKOFF_TIME)
                print(f"Waiting {backoff_time} seconds before retry (attempt {attempt + 1}/{MAX_RETRIES})...")
                time.sleep(backoff_time)

    def choose_action(self, scenario: Dict, weirdness_level: int) -> int:
        """Have the LLM choose an action based on the scenario"""
        prompt = self._create_prompt(scenario, weirdness_level)
        response = self._make_api_call(prompt)
        
        # Extract the chosen option number from the response
        # This is a simple implementation - could be made more robust
        for i in range(len(scenario['choices'])):
            if str(i + 1) in response.split()[0]:
                return i
        
        # Default to first choice if no clear choice is found
        return 0
