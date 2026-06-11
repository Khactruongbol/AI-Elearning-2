"""Run the Dining Philosophers CSP solver."""

import argparse

from model import build_problem, trace_constraints
from solver import format_solution, max_eating_count, solve


def main():
    parser = argparse.ArgumentParser(description="Solve Dining Philosophers as CSP")
    parser.add_argument("-n", "--philosophers", type=int, default=5)
    parser.add_argument("--trace", action="store_true")
    args = parser.parse_args()

    philosophers, domains, adjacency = build_problem(args.philosophers)
    solution = solve(args.philosophers)

    print(f"EL02 - Dining Philosophers Problem (n={len(philosophers)})")
    print(f"Domain = {domains[philosophers[0]]}")
    print(f"Maximum Eating = {max_eating_count(len(philosophers))}")
    print()
    print(format_solution(solution))

    if args.trace:
        print()
        trace_constraints(solution, adjacency)


if __name__ == "__main__":
    main()
