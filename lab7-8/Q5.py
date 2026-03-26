from ortools.sat.python import cp_model

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        super().__init__()
        self._vars = variables
        self.total = 0

    def on_solution_callback(self):
        self.total += 1
        assignment = {v.name: self.value(v) for v in self._vars}
        print(f"  Solution {self.total}: {assignment}")


csp2 = cp_model.CpModel()
p2 = csp2.new_int_var(0, 3, "P")
q2 = csp2.new_int_var(0, 3, "Q")
r2 = csp2.new_int_var(0, 3, "R")
csp2.add(p2 != q2)
csp2.add(q2 != r2)
csp2.add(p2 + q2 <= 4)

solver2 = cp_model.CpSolver()
printer = SolutionPrinter([p2, q2, r2])
solver2.parameters.enumerate_all_solutions = True
solver2.solve(csp2, printer)

print(f"\nTotal valid assignments: {printer.total}")
