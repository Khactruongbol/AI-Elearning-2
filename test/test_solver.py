import sys
import unittest
from pathlib import Path


SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from model import DOMAIN, EATING, build_problem, is_valid_assignment, not_both_eating
from solver import count_eating, max_eating_count, solve


class DiningPhilosophersTest(unittest.TestCase):
    def test_build_problem_n5(self):
        philosophers, domains, adjacency = build_problem(5)

        self.assertEqual(["P1", "P2", "P3", "P4", "P5"], philosophers)
        self.assertEqual(DOMAIN, domains["P1"])
        self.assertEqual(["P5", "P2"], adjacency["P1"])
        self.assertEqual(["P4", "P1"], adjacency["P5"])

    def test_not_both_eating_constraint(self):
        self.assertFalse(not_both_eating(EATING, EATING))
        self.assertTrue(not_both_eating(EATING, "Thinking"))
        self.assertTrue(not_both_eating("Thinking", EATING))

    def test_solution_for_n5_is_valid_and_complete(self):
        philosophers, _, adjacency = build_problem(5)
        solution = solve(5)

        self.assertEqual(set(philosophers), set(solution))
        self.assertTrue(is_valid_assignment(solution, adjacency))
        self.assertEqual(2, count_eating(solution))

    def test_solver_maximizes_eating_count_for_many_n(self):
        for n in range(2, 11):
            philosophers, _, adjacency = build_problem(n)
            solution = solve(n)

            self.assertEqual(set(philosophers), set(solution))
            self.assertTrue(is_valid_assignment(solution, adjacency))
            self.assertEqual(max_eating_count(n), count_eating(solution))


if __name__ == "__main__":
    unittest.main()
