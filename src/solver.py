"""Simple solver for the Dining Philosophers CSP."""

from model import EATING, THINKING, build_problem, is_valid_assignment


def max_eating_count(n):
    """Maximum number of non-adjacent Eating philosophers in a cycle."""

    if n < 2:
        raise ValueError("n must be at least 2")
    return n // 2


def solve(n=5):
    """Return a complete assignment with floor(n/2) philosophers Eating."""

    philosophers, domains, adjacency = build_problem(n)
    target = max_eating_count(n)
    solution = backtrack(philosophers, domains, adjacency, {}, target)

    if solution is None:
        raise RuntimeError("No valid assignment found")

    return solution


def backtrack(philosophers, domains, adjacency, assignment, target):
    if len(assignment) == len(philosophers):
        if count_eating(assignment) == target:
            return assignment.copy()
        return None

    philosopher = philosophers[len(assignment)]

    # Try Eating first so the solution is non-trivial and reaches floor(n/2).
    for state in [EATING, THINKING]:
        assignment[philosopher] = state

        if (
            state in domains[philosopher]
            and is_valid_assignment(assignment, adjacency)
            and count_eating(assignment) <= target
            and can_still_reach_target(philosophers, assignment, target)
        ):
            result = backtrack(philosophers, domains, adjacency, assignment, target)
            if result is not None:
                return result

        del assignment[philosopher]

    return None


def can_still_reach_target(philosophers, assignment, target):
    remaining = len(philosophers) - len(assignment)
    return count_eating(assignment) + remaining >= target


def count_eating(assignment):
    return sum(1 for state in assignment.values() if state == EATING)


def format_solution(assignment):
    lines = ["Dining Philosophers complete assignment:"]
    for philosopher in sorted(assignment, key=lambda name: int(name[1:])):
        lines.append(f"{philosopher} = {assignment[philosopher]}")
    lines.append(f"Eating count = {count_eating(assignment)}")
    return "\n".join(lines)


def verify(assignment):
    philosophers = list(assignment)
    adjacency = {}
    for i, philosopher in enumerate(philosophers):
        adjacency[philosopher] = [
            philosophers[(i - 1) % len(philosophers)],
            philosophers[(i + 1) % len(philosophers)],
        ]
    return is_valid_assignment(assignment, adjacency)


if __name__ == "__main__":
    solution = solve(5)
    print(format_solution(solution))
