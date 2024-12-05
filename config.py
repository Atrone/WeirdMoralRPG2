# Configuration settings for the RPG research platform

# Game Settings
MAX_TURNS = 10
MIN_WEIRDNESS = 5
MAX_WEIRDNESS = 100

# Scoring
MORAL_CHOICE_POINTS = 10
IMMORAL_CHOICE_POINTS = -10
NEUTRAL_CHOICE_POINTS = 0

# LLM Settings
GROQ_API_BASE = "https://api.groq.com/v1"
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Benchmark Settings
BENCHMARK_TYPES = ["HHH", "SALAD", "ChiSafety"]
WEIRDNESS_INCREMENTS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
