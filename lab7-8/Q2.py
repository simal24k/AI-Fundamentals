import math

pruned_nodes = []
ab_visit_log = []
 
 
def alpha_beta(tree, node, depth, alpha, beta, maximising):
    ab_visit_log.append(node)
 
    children = tree.get(node, [])
    if not children or depth == 0:
        return node
 
    if maximising:
        best = -math.inf
        for ch in children:
            score = alpha_beta(tree, ch, depth - 1, alpha, beta, False)
            best  = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:
                pruned_nodes.append(ch)
                break     
        return best
    else:
        best = math.inf
        for ch in children:
            score = alpha_beta(tree, ch, depth - 1, alpha, beta, True)
            best  = min(best, score)
            beta  = min(beta, best)
            if beta <= alpha:
                pruned_nodes.append(ch)
                break  
        return best
 
 
pruned_nodes.clear()
ab_visit_log.clear()
ab_score = alpha_beta(game_tree, "ROOT", 3, -math.inf, math.inf, True)


print(f"Root value        : {ab_score}")
print(f"Nodes visited     : {len(ab_visit_log)}  (vs {len(visit_log)} in plain Minimax)")
print(f"Pruned at         : {pruned_nodes}")
print("\nWhy pruning helps: once we know a branch can't affect the final")
print("decision (α ≥ β), we skip it entirely — fewer nodes, same result.")
