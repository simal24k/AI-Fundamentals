import math
game_tree = {
    "ROOT": ["N1", "N2"],
    "N1":   ["N3", "N4"],
    "N2":   ["N5", "N6"],
    "N3":   [4, 7],
    "N4":   [2, 5],
    "N5":   [1, 8],
    "N6":   [3, 6],
    4: [], 7: [], 2: [], 5: [],
    1: [], 8: [], 3: [], 6: [],
}
 
visit_log = [] 
 
def minimax(tree, node, depth, maximising):
    """Standard minimax – no pruning."""
    visit_log.append(node)
 
    children = tree.get(node, [])
    if not children or depth == 0:
        return node 
 
    child_scores = [minimax(tree, ch, depth - 1, not maximising)
                    for ch in children]
 
    return max(child_scores) if maximising else min(child_scores)

visit_log.clear()
root_score = minimax(game_tree, "ROOT", depth=3, maximising=True)
 

print(f"Root value (full tree) : {root_score}")
print(f"Visit order            : {visit_log}")
 
visit_log.clear()
limited_score = minimax(game_tree, "ROOT", depth=2, maximising=True)
print(f"\nDepth-limited (d=2) root value : {limited_score}")
print(f"Visit order (d=2)              : {visit_log}")
