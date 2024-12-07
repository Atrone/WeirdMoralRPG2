from game_engine import GameEngine
from llm_player import LLMPlayer
from benchmarks import BenchmarkRunner
from metrics import MoralityTracker
from config import WEIRDNESS_INCREMENTS, BENCHMARK_TYPES
import argparse
import os


def run_llm_experiment(api_key: str, output_dir: str):
    """Run the complete LLM experiment"""
    # Initialize components
    llm_player = LLMPlayer(api_key)
    benchmark_runner = BenchmarkRunner(llm_player)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Run game benchmarks at different weirdness levels
    game_results = []
    total_levels = len(WEIRDNESS_INCREMENTS)
    print(f"\nStarting LLM experiment with {total_levels} weirdness levels...")
    
    for i, weirdness_level in enumerate(WEIRDNESS_INCREMENTS, 1):
        print(f"\nProcessing weirdness level {weirdness_level} ({i}/{total_levels})")
        result = benchmark_runner.run_game_benchmark(weirdness_level)
        print(f"Completed weirdness level {weirdness_level} - "
              f"Moral score: {result.get('moral_score', 0)}, "
              f"Capability score: {result.get('capability_score', 0)}")
        game_results.append(result)

    # Run standard benchmarks
    benchmark_results = []
    for benchmark_type in BENCHMARK_TYPES:
        results = benchmark_runner.run_standard_benchmarks(
            benchmark_type, WEIRDNESS_INCREMENTS)
        benchmark_results.extend(results)

    # Export results
    for result in game_results:
        morality_tracker = result.get('game').morality_tracker if hasattr(result.get('game', {}), 'morality_tracker') else MoralityTracker()
        morality_tracker.export_csv(f"{output_dir}/morality_scores_{result['weirdness_level']}.csv")
        morality_tracker.export_json(f"{output_dir}/morality_scores_{result['weirdness_level']}.json")
    
    # Export benchmark results
    with open(f"{output_dir}/benchmark_results.json", 'w') as f:
        json.dump(benchmark_results, f, indent=2)


def run_human_game():
    """Run the game in human-playable mode"""
    game = GameEngine(weirdness_level=0)

    while not game.is_game_over():
        scenario = game.get_current_scenario()
        print("\n" + scenario["description"])

        print("\nChoices:")
        for i, choice in enumerate(scenario["choices"]):
            print(f"{i + 1}. {choice['text']}")

        while True:
            try:
                choice = int(input("\nEnter your choice (1-3): ")) - 1
                if 0 <= choice < len(scenario["choices"]):
                    break
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")

        result, moral_delta, capability_delta = game.make_choice(choice)
        print(f"\n{result}")
        print(f"Moral score change: {moral_delta}")
        print(f"Capability score change: {capability_delta}")

    final_scores = game.get_final_scores()
    print("\nGame Over!")
    print(f"Final moral score: {final_scores['moral_score']}")
    print(f"Final capability score: {final_scores['capability_score']}")


def main():
    parser = argparse.ArgumentParser(description="RPG Research Platform")
    parser.add_argument(
        "--mode",
        choices=["llm", "human"],
        required=True,
        help="Run in LLM experiment mode or human-playable mode")
    parser.add_argument("--api-key", help="Groq API key for LLM mode")
    parser.add_argument("--output-dir",
                        default="results",
                        help="Directory for experiment results")

    args = parser.parse_args()

    if args.mode == "llm":
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            print("Error: GROQ_API_KEY environment variable is not set")
            return
        run_llm_experiment(api_key, args.output_dir)
    else:
        run_human_game()


if __name__ == "__main__":
    main()
