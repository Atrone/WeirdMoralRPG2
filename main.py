from game_engine import GameEngine
from llm_player import LLMPlayer
import json
from benchmarks import BenchmarkRunner
from metrics import MoralityTracker
from config import WEIRDNESS_INCREMENTS, BENCHMARK_TYPES, LOCAL, MODEL
import argparse
import os


def run_llm_experiment(api_key: str, output_dir: str):
    """Run the complete LLM experiment"""
    # Initialize components
    llm_player = LLMPlayer(api_key, model=MODEL,
                           use_local_model=LOCAL)  #Updated model here
    benchmark_runner = BenchmarkRunner(llm_player)

    # Create output directory if it doesn't exist
    try:
        os.makedirs(output_dir, exist_ok=True)
        print(f"Created output directory at: {os.path.abspath(output_dir)}")
    except Exception as e:
        print(f"Error creating output directory: {str(e)}")
        raise

    # Run game benchmarks at different weirdness levels
    game_results = []
    total_levels = len(WEIRDNESS_INCREMENTS)
    print(f"\nStarting LLM experiment with {total_levels} weirdness levels...")

    for i, weirdness_level in enumerate(WEIRDNESS_INCREMENTS, 1):
        print(
            f"\nProcessing weirdness level {weirdness_level} ({i}/{total_levels})"
        )
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

    # Generate comprehensive analysis report
    print("\nGenerating comprehensive analysis report...")
    analysis_report = benchmark_runner.generate_comprehensive_report(
        game_results, benchmark_results)

    # Export results
    game_results_path = os.path.abspath(f"{output_dir}/game_results.json")
    benchmark_results_path = os.path.abspath(
        f"{output_dir}/benchmark_results.json")

    try:
        print(f"Writing game results to: {game_results_path}")
        with open(game_results_path, 'w') as f:
            json.dump([{
                'weirdness_level': r['weirdness_level'],
                'moral_score': r['moral_score'],
                'capability_score': r['capability_score'],
                'turns_taken': r['turns_taken'],
                'choices': r.get('choices', [])
            } for r in game_results],
                      f,
                      indent=2)
    except Exception as e:
        print(f"Error writing game results: {str(e)}")
        raise

    try:
        print(f"Writing benchmark results to: {benchmark_results_path}")
        with open(benchmark_results_path, 'w') as f:
            json.dump(benchmark_results, f, indent=2)
    except Exception as e:
        print(f"Error writing benchmark results: {str(e)}")
        raise

    # Save analysis report
    benchmark_runner.save_analysis_report(analysis_report, output_dir)
    print(
        f"\nAnalysis report saved to: {os.path.abspath(f'{output_dir}/analysis_report.json')}"
    )

    # Print key findings
    print("\nKey Findings:")

    print(f"Model: {llm_player.model}")
    print(
        f"Total games analyzed: {analysis_report['overall_findings']['total_games']}"
    )
    print(
        f"Average moral score: {analysis_report['overall_findings']['average_moral_score']:.2f}"
    )
    print(
        f"Moral score standard deviation: {analysis_report['overall_findings']['moral_score_std']:.2f}"
    )
    print(
        f"Benchmark effectiveness: {analysis_report['overall_findings']['benchmark_effectiveness']:.2f}"
    )


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
        llm_player = LLMPlayer(api_key=api_key, use_local_model=False)
        run_llm_experiment(api_key, args.output_dir)
    else:
        run_human_game()


if __name__ == "__main__":
    main()
