
import sys
sys.path.insert(0, '/mnt/user-data/outputs')
 
from dining_philosophers_solver import (
    constructive_solve,
    backtracking_solve,
    verify,
    EATING, THINKING,
)
 
PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
 
results = []
 
def check(name: str, condition: bool) -> None:
    status = PASS if condition else FAIL
    print(f"  [{status}] {name}")
    results.append(condition)
 
 
print("\n== 1. verify() — constraint checker ==")
 
check("n=4 all Thinking is valid",
      verify([THINKING]*4, 4))
 
check("n=4 two adjacent Eating is invalid",
      not verify([EATING, EATING, THINKING, THINKING], 4))
 
check("n=4 wrap-around violation [E,T,T,E] at edge (P4,P1) — invalid",
      not verify([EATING, THINKING, THINKING, EATING], 4))
 
check("n=5 valid assignment [E,T,E,T,T]",
      verify([EATING,THINKING,EATING,THINKING,THINKING], 5))
 
 
print("\n== 2. constructive_solve() ==")
 
for n in range(3, 13):
    sol = constructive_solve(n)
    eating = sol.count(EATING)
    check(f"n={n:>2}: valid assignment",          verify(sol, n))
    check(f"n={n:>2}: achieves floor(n/2)={n//2}", eating == n // 2)
    check(f"n={n:>2}: non-trivial (not all T)",   any(s == EATING for s in sol))
 
 
print("\n== 3. backtracking_solve() ==")
 
for n in range(3, 13):
    sol, stats = backtracking_solve(n)
    eating = sol.count(EATING)
    check(f"n={n:>2}: valid assignment",           verify(sol, n))
    check(f"n={n:>2}: achieves floor(n/2)={n//2}", eating == n // 2)
    check(f"n={n:>2}: non-trivial (not all T)",    any(s == EATING for s in sol))
    check(f"n={n:>2}: nodes_visited > 0",          stats.nodes_visited > 0)
 
 
print("\n== 4. Both solvers agree ==")
 
for n in range(3, 13):
    sol_c  = constructive_solve(n)
    sol_bt, _ = backtracking_solve(n)
    check(f"n={n:>2}: same eating count",
          sol_c.count(EATING) == sol_bt.count(EATING))
 
 
print("\n== 5. Edge cases ==")
 
sol3 = constructive_solve(3)
check("n=3: floor(3/2)=1 Eating", sol3.count(EATING) == 1)
check("n=3: valid", verify(sol3, 3))
 
sol3bt, _ = backtracking_solve(3)
check("n=3 BT: floor(3/2)=1 Eating", sol3bt.count(EATING) == 1)
check("n=3 BT: valid", verify(sol3bt, 3))
 
sol_large = constructive_solve(20)
check("n=20: achieves 10 Eating", sol_large.count(EATING) == 10)
check("n=20: valid", verify(sol_large, 20))
 
sol_large_bt, _ = backtracking_solve(20)
check("n=20 BT: achieves 10 Eating", sol_large_bt.count(EATING) == 10)
check("n=20 BT: valid", verify(sol_large_bt, 20))
 
 
passed = sum(results)
total  = len(results)
print(f"\n{'='*40}")
print(f"  Result: {passed}/{total} tests passed")
print(f"{'='*40}\n")
sys.exit(0 if passed == total else 1)