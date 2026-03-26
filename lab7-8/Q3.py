import math
modified_tree = {
    "ROOT": ["N1", "N2"],
    "N1":   ["N3", "N4"],
    "N2":   ["N5", "N6"],
    "N3":   [4, 9, 2],  
    "N4":   [6, 1],
    "N5":   [5, 3],
    "N6":   [7, 0],
    4: [], 9: [], 2: [],
    6: [], 1: [], 5: [],
    3: [], 7: [], 0: [],
}
 
 
def minimax_path(tree, node, maximising):
    children = tree.get(node, [])
    if not children:
        return node, [node]
 
    results = [(minimax_path(tree, ch, not maximising), ch)
               for ch in children]
 
    if maximising:
        (score, sub_path), chosen = max(results, key=lambda r: r[0][0])
    else:
        (score, sub_path), chosen = min(results, key=lambda r: r[0][0])
 
    return score, [node] + sub_path
 
 
def alpha_beta_mod(tree, node, alpha, beta, maximising, pruned):
    children = tree.get(node, [])
    if not children:
        return node
 
    if maximising:
        best = -math.inf
        for ch in children:
            val  = alpha_beta_mod(tree, ch, alpha, beta, False, pruned)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                pruned.append(ch)
                break
        return best
    else:
        best = math.inf
        for ch in children:
            val  = alpha_beta_mod(tree, ch, alpha, beta, True, pruned)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                pruned.append(ch)
                break
        return best
 
 
mod_score, optimal_path = minimax_path(modified_tree, "ROOT", True)
mod_pruned = []
ab_mod_score = alpha_beta_mod(modified_tree, "ROOT", -math.inf, math.inf, True, mod_pruned)
 
print(f"Minimax root value  : {mod_score}")
print(f"Alpha-Beta root     : {ab_mod_score}")
print(f"Optimal path (Max)  : {' → '.join(str(n) for n in optimal_path)}")
print(f"Pruned nodes        : {mod_pruned}")
print("\nObservation: adding a third child to N3 (value 9) raises N3's score")
print("to 9, which changes the subtree outcome. Pruning behaviour shifts")
print("because new α/β thresholds are established earlier in the search.")
