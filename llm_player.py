import time
import random
import requests
from typing import Dict, Optional, List
from datetime import datetime, timedelta
from config import GROQ_API_BASE, MAX_RETRIES, RETRY_DELAY, RATE_LIMIT_DELAY, MAX_BACKOFF_TIME

class RequestTracker:
    def __init__(self, window_size: int = 60):
        self.requests: List[datetime] = []
        self.window_size = window_size  # Time window in seconds

    def add_request(self):
        """Record a new request"""
        now = datetime.now()
        self.requests.append(now)
        # Clean up old requests
        self.requests = [t for t in self.requests if now - t < timedelta(seconds=self.window_size)]

    def get_request_count(self) -> int:
        """Get number of requests in current window"""
        self.add_request()  # This will also clean up old requests
        return len(self.requests)

    def should_throttle(self, max_requests: int = 50) -> bool:
        """Check if we should throttle based on recent request count"""
        return self.get_request_count() >= max_requests

class LLMPlayer:
    def __init__(self, api_key: str, model: str = "mixtral-8x7b-32768"):
        self.api_key = api_key
        self.model = model
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.request_tracker = RequestTracker()
        self.successful_requests = 0
        self.failed_requests = 0

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

    def _add_jitter(self, delay: float, jitter_factor: float = 0.1) -> float:
        """Add random jitter to delay to prevent thundering herd"""
        jitter = random.uniform(-delay * jitter_factor, delay * jitter_factor)
        return max(0.1, delay + jitter)

    def _handle_rate_limit_error(self, attempt: int) -> float:
        """Handle rate limit error with exponential backoff"""
        base_delay = RATE_LIMIT_DELAY
        backoff_time = min(base_delay * (2 ** attempt), MAX_BACKOFF_TIME)
        return self._add_jitter(backoff_time)

    def _handle_other_error(self, attempt: int, status_code: Optional[int]) -> float:
        """Handle other errors with appropriate delays"""
        if status_code in [500, 502, 503, 504]:
            # Server errors: use moderate delay
            base_delay = RETRY_DELAY * 2
        else:
            # Other errors: use standard delay
            base_delay = RETRY_DELAY
        backoff_time = min(base_delay * (2 ** attempt), MAX_BACKOFF_TIME)
        return self._add_jitter(backoff_time)

    def _make_api_call(self, prompt: str) -> Optional[str]:
        """Make API call to Groq with improved error handling and rate limiting"""
        # Check if we should throttle requests
        if self.request_tracker.should_throttle():
            print("Rate limit approaching, adding delay...")
            time.sleep(RETRY_DELAY)

        for attempt in range(MAX_RETRIES):
            try:
                print(f"Attempting API call to {GROQ_API_BASE}")
                
                # Record request attempt
                self.request_tracker.add_request()
                
                response = requests.post(
                    f"{GROQ_API_BASE}/chat/completions",
                    headers=self.headers,
                    json={
                        "model": self.model,
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.7
                    }
                )
                
                # Handle different status codes
                if response.status_code == 200:
                    print(f"API call successful (Total successful: {self.successful_requests + 1})")
                    self.successful_requests += 1
                    return response.json()["choices"][0]["message"]["content"]
                
                response.raise_for_status()
                
            except requests.exceptions.HTTPError as e:
                status_code = e.response.status_code if hasattr(e, 'response') else None
                error_type = "Rate limit" if status_code == 429 else f"HTTP {status_code}"
                print(f"{error_type} error: {str(e)}")
                
                if attempt == MAX_RETRIES - 1:
                    self.failed_requests += 1
                    raise e
                
                # Calculate backoff time based on error type
                if status_code == 429:
                    delay = self._handle_rate_limit_error(attempt)
                else:
                    delay = self._handle_other_error(attempt, status_code)
                
                print(f"Waiting {delay:.2f} seconds before retry (attempt {attempt + 1}/{MAX_RETRIES})...")
                time.sleep(delay)
                
            except Exception as e:
                print(f"Unexpected error: {str(e)}")
                if attempt == MAX_RETRIES - 1:
                    self.failed_requests += 1
                    raise e
                
                delay = self._handle_other_error(attempt, None)
                print(f"Waiting {delay:.2f} seconds before retry (attempt {attempt + 1}/{MAX_RETRIES})...")
                time.sleep(delay)

    def choose_action(self, scenario: Dict, weirdness_level: int) -> int:
        """Have the LLM choose an action based on the scenario"""
        prompt = self._create_prompt(scenario, weirdness_level)
        response = self._make_api_call(prompt)
        
        if not response:
            print("Warning: No response from API, defaulting to first choice")
            return 0
        
        # Extract the chosen option number from the response
        # This is a simple implementation - could be made more robust
        for i in range(len(scenario['choices'])):
            if str(i + 1) in response.split()[0]:
                return i
        
        # Default to first choice if no clear choice is found
        return 0

    def get_stats(self) -> Dict:
        """Get current request statistics"""
        return {
            "successful_requests": self.successful_requests,
            "failed_requests": self.failed_requests,
            "recent_requests": self.request_tracker.get_request_count()
        }
