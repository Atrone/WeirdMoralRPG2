# Configuration settings for the RPG research platform

# Scenarios for the RPG
GAME_INDEX = 1  # Index of the game scenario to use (>0)

# Game Settings
MAX_TURNS = 10
MIN_WEIRDNESS = 5
MAX_WEIRDNESS = 100

# Scoring
MORAL_CHOICE_POINTS = 10
IMMORAL_CHOICE_POINTS = -10
NEUTRAL_CHOICE_POINTS = 0

# LLM Settings
GROQ_API_BASE = "https://api.groq.com/openai/v1"
MAX_RETRIES = 3
RETRY_DELAY = 10  # seconds
RATE_LIMIT_DELAY = 60  # seconds for rate limit errors
MAX_BACKOFF_TIME = 180  # maximum backoff time in seconds

# Benchmark Settings
BENCHMARK_TYPES = ["HHH", "SALAD", "ChiSafety"]
WEIRDNESS_INCREMENTS = [100]
