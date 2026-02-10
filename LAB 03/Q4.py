def restaurant_selector():
    options = [('A', 3, 10), ('B', 4, 9)]
    scores = []
    for name, dist, rate in options:
        util = rate - dist
        print(f"Restaurant {name} Utility = {util}")
        scores.append((util, name))
    
    scores.sort(reverse=True)
    print(f"Selected Restaurant: {scores[0][1]}")

restaurant_selector()
