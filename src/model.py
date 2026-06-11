"""Simple CSP model helpers for the Dining Philosophers Problem."""

THINKING = "Thinking"
EATING = "Eating"
DOMAIN = [THINKING, EATING]


def build_problem(n=5):
    """Create philosophers, domains, and circular adjacency list."""

    if n < 2:
        raise ValueError("n must be at least 2")

    philosophers = [f"P{i}" for i in range(1, n + 1)]
    domains = {philosopher: DOMAIN[:] for philosopher in philosophers}
    adjacency = build_adjacency_list(philosophers)
    return philosophers, domains, adjacency


def build_adjacency_list(philosophers):
    """Each Pi is adjacent to P(i-1) and P(i+1), using circular indexing."""

    n = len(philosophers)
    adjacency = {}
    for i, philosopher in enumerate(philosophers):
        left = philosophers[(i - 1) % n]
        right = philosophers[(i + 1) % n]
        adjacency[philosopher] = [left, right]
    return adjacency


def not_both_eating(value_i, value_j):
    """CSP constraint: not (Pi = Eating and Pj = Eating)."""

    return not (value_i == EATING and value_j == EATING)


def is_valid_assignment(assignment, adjacency):
    """Check all assigned neighbor pairs in the circular table."""

    checked = set()
    for philosopher, neighbors in adjacency.items():
        for neighbor in neighbors:
            pair = tuple(sorted([philosopher, neighbor]))
            if pair in checked:
                continue
            checked.add(pair)

            if philosopher not in assignment or neighbor not in assignment:
                continue

            if not not_both_eating(assignment[philosopher], assignment[neighbor]):
                return False
    return True


def trace_constraints(assignment, adjacency):
    """Print a simple trace for each neighbor constraint."""

    print("TRACE KIEM TRA RANG BUOC - Dining Philosophers CSP")
    print("\nAssignment:")
    for philosopher, state in assignment.items():
        print(f"  {philosopher} = {state}")

    print("\nKiem tra tung rang buoc:")
    checked = set()
    all_ok = True
    violated = []

    for philosopher, neighbors in adjacency.items():
        for neighbor in neighbors:
            pair = tuple(sorted([philosopher, neighbor]))
            if pair in checked:
                continue
            checked.add(pair)

            value_i = assignment.get(philosopher)
            value_j = assignment.get(neighbor)
            if value_i is None or value_j is None:
                print(f"  {philosopher}--{neighbor}: chua gan du, bo qua")
                continue

            ok = not_both_eating(value_i, value_j)
            status = "THOA" if ok else "VI PHAM"
            print(f"  {philosopher}={value_i:<8} | {neighbor}={value_j:<8} -> {status}")

            if not ok:
                all_ok = False
                violated.append(f"{philosopher}-{neighbor}")

    if all_ok:
        print("\nKET LUAN: Assignment HOP LE\n")
    else:
        print(f"\nKET LUAN: VI PHAM tai cap: {', '.join(violated)}\n")

    return all_ok
