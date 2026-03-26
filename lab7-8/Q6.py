opt = cp_model.CpModel()
xv = opt.new_int_var(0, 20, "x")
yv = opt.new_int_var(0, 20, "y")
zv = opt.new_int_var(0, 20, "z")
 
opt.add(xv + 2 * yv + zv <= 20)
opt.add(3 * xv + yv <= 18)
opt.maximize(4 * xv + 2 * yv + zv)
 
solver3 = cp_model.CpSolver()
solver3.solve(opt)
 
print(f"x = {solver3.value(xv)}")
print(f"y = {solver3.value(yv)}")
print(f"z = {solver3.value(zv)}")
print(f"Optimal objective value: {int(solver3.objective_value)}")
