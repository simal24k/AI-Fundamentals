board_size = 4
queens_model = cp_model.CpModel()
 
col = [queens_model.new_int_var(0, board_size - 1, f"row{i}")
       for i in range(board_size)]
 
queens_model.add_all_different(col)
 
queens_model.add_all_different([col[i] + i for i in range(board_size)])
queens_model.add_all_different([col[i] - i for i in range(board_size)])
 
solver4 = cp_model.CpSolver()
solver4.solve(queens_model)
 
for row_idx in range(board_size):
    line = ""
    for col_idx in range(board_size):
        line += "Q " if solver4.value(col[row_idx]) == col_idx else "_ "
    print(line.strip())
