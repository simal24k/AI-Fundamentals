import numpy as np

states = ['Sunny', 'Cloudy', 'Rainy']

transition = np.array([
    [0.60, 0.30, 0.10],
    [0.30, 0.40, 0.30],
    [0.20, 0.30, 0.50]
])

print("\nTransition Matrix:")
print(f"{'':10} {'Sunny':>8} {'Cloudy':>8} {'Rainy':>8}")
for i, s in enumerate(states):
    row = "   ".join(f"{v:8.2f}" for v in transition[i])
    print(f"{s:10} {row}")

np.random.seed(42)
current_state = 0  # Sunny
weather_sequence = [states[current_state]]

for _ in range(9):
    current_state = np.random.choice(3, p=transition[current_state])
    weather_sequence.append(states[current_state])

print(f"\nSimulated 10-Day Weather Sequence (starting Sunny):")
for day, w in enumerate(weather_sequence, 1):
    print(f"  Day {day:2d}: {w}")

rainy_count = weather_sequence.count('Rainy')
print(f"\nNumber of Rainy days in simulation: {rainy_count}")

n_simulations = 100000
rainy_days_counts = []

for _ in range(n_simulations):
    state = 0
    rainy = 0
    for _ in range(10):
        if states[state] == 'Rainy':
            rainy += 1
        state = np.random.choice(3, p=transition[state])
    rainy_days_counts.append(rainy)

rainy_array = np.array(rainy_days_counts)
p_at_least_3 = np.mean(rainy_array >= 3)
print(f"\nP(at least 3 Rainy days in 10 days) \u2248 {p_at_least_3:.4f}")
print(f"  (Estimated via {n_simulations:,} Monte Carlo simulations)")
