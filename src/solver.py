
from dataclasses import dataclass, field
 
EATING, THINKING = "Eating", "Thinking"
  
def is_consistent(assignment: list, idx: int, n: int) -> bool:
    """
    Returns False if assignment[idx] = Eating violates a constraint.
    Only checks left neighbor and the wrap-around edge (when idx = n-1).
    """
    if assignment[idx] != EATING:
        return True
    if idx > 0 and assignment[idx - 1] == EATING:
        return False
    if idx == n - 1 and assignment[0] == EATING:
        return False
    return True
 
 
def constructive_solve(n: int) -> list:
    """
    Builds a solution directly in O(n) achieving floor(n/2) Eating.
 
    Base pattern: E T E T E T ...
    - n even: [E,T,E,T,...,E,T]   → n/2 Eating, no cycle violation.
    - n odd:  [E,T,E,T,...,E,T,T] → floor(n/2) Eating.
              P_{n-1} must be T because P_0 = E and they are adjacent on the cycle.
    """
    assignment = [EATING if i % 2 == 0 else THINKING for i in range(n)]
    if n % 2 == 1:
        assignment[n - 1] = THINKING  
    return assignment
 
 
@dataclass
class BTStats:
    nodes_visited: int = 0
    prune_count:   int = 0
    backtracks:    int = 0
    best_eating:   int = 0
    best_solution: list = field(default_factory=list)
 
 
def backtracking_solve(n: int) -> tuple:
    """
    CSP Backtracking with:
      - Value ordering: [Eating, Thinking]  → non-trivial solutions prioritized
      - Forward checking: constraint tested immediately on assignment
      - Early termination: stops as soon as floor(n/2) Eating is reached
 
    Returns (best_solution, BTStats).
    """
    assignment = [None] * n
    target     = n // 2
    stats      = BTStats()
 
    def _bt(idx: int) -> bool:
        if idx == n:                     
            stats.nodes_visited += 1
            eating = assignment.count(EATING)
            if eating > stats.best_eating:
                stats.best_eating   = eating
                stats.best_solution = assignment[:]
            return eating >= target        
 
        for value in [EATING, THINKING]:     
            stats.nodes_visited += 1
            assignment[idx] = value
 
            if is_consistent(assignment, idx, n):
                if _bt(idx + 1):
                    return True             
            else:
                stats.prune_count += 1
 
        stats.backtracks += 1
        assignment[idx] = None
        return False
 
    _bt(0)
 
    if not stats.best_solution:
        stats.best_solution = [THINKING] * n
 
    return stats.best_solution, stats
 

 
def verify(assignment: list, n: int) -> bool:
    return all(
        not (assignment[i] == EATING and assignment[(i + 1) % n] == EATING)
        for i in range(n)
    )
 
 
def print_result(n: int, assignment: list, method: str, stats: BTStats = None) -> None:
    sep = "─" * 52
    eating  = assignment.count(EATING)
    print(f"\n{sep}")
    print(f"  n={n}  |  {method}  |  floor(n/2)={n//2}")
    print(sep)
    for i, s in enumerate(assignment):
        print(f"  P{i+1:>2}: {'●' if s == EATING else '○'} {s}")
    print(f"\n  Eating: {eating}/{n}  |  Valid: {verify(assignment, n)}  |  Optimal: {eating == n//2}")
    if stats:
        print(f"  Nodes: {stats.nodes_visited}  |  Pruned: {stats.prune_count}  |  Backtracks: {stats.backtracks}")
    print(sep)
 
 
 
if __name__ == "__main__":
    print("=" * 52)
    print("  DINING PHILOSOPHERS CSP SOLVER")
    print("=" * 52)
 
    for n in [5, 6, 7, 8]:
        print_result(n, constructive_solve(n), "Constructive O(n)")
        sol, stats = backtracking_solve(n)
        print_result(n, sol, "Backtracking + Forward Checking", stats)