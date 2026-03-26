from ortools.sat.python import cp_model
 
csp = cp_model.CpModel()
 
p = csp.new_int_var(0, 3, "P") 
q = csp.new_int_var(0, 3, "Q") 
r = csp.new_int_var(0, 3, "R") 
 
csp.add(p != q)        
csp.add(q != r)        
csp.add(p + q <= 4)    
 
solver = cp_model.CpSolver()
status = solver.solve(csp)
 
if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
    print(f"P = {solver.value(p)}")
    print(f"Q = {solver.value(q)}")
    print(f"R = {solver.value(r)}")
else:
    print("No solution found.")
