import argparse

SCORES = {"alice": 91, "bob": 78, "carol": 85}


def get_results(min_score):
    return {k: v for k, v in sorted(SCORES.items()) if v >= min_score}


def print_table(results):
    print(f"{'name':<10}{'score':>6}")
    for name, score in results.items():
        print(f"{name:<10}{score:>6}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Show scores")
    parser.add_argument("--min", type=int, default=0, help="minimum score")
    args = parser.parse_args(argv)
    print_table(get_results(args.min))


if __name__ == "__main__":
    main()
