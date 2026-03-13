#Hill Climbing
import random

def f(x):
    return -x**2 + 6*x

x = random.randint(0, 6)
print(f"Initial x = {x}, f(x) = {f(x)}")

step = 1
while True:
    curr = f(x)
    left  = f(x - 1) if x - 1 >= 0 else float('-inf')
    right = f(x + 1) if x + 1 <= 6 else float('-inf')

    best = max(left, right)
    if best <= curr:
        break

    x = x - 1 if left > right else x + 1
    print(f"Step {step}: x = {x}, f(x) = {f(x)}")
    step += 1

print(f"\nOptimal x = {x}, f(x) = {f(x)}")
