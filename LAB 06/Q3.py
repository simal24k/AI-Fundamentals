#Genetic Algo
import random

def fitness(x):
    return x*x + 2*x

pop_size = 6
gens = 15
mutrate = 0.1

def decode(b):
    return int(b, 2)

def encode(x):
    return format(x, '05b')

def new_chr():
    return ''.join([random.choice(['0','1']) for _ in range(5)])

def tournament(pop):
    p1 = random.choice(pop)
    p2 = random.choice(pop)
    if fitness(decode(p1)) >= fitness(decode(p2)):
        return p1
    return p2

def cross(p1, p2):
    cut = random.randint(1, 4)
    return p1[:cut] + p2[cut:]

def mutate(ch):
    result = ''
    for bit in ch:
        if random.random() < mutrate:
            result += '1' if bit == '0' else '0'
        else:
            result += bit
    return result

# main

pop = [new_chr() for _ in range(pop_size)]

for g in range(1, gens + 1):
    pop.sort(key=lambda c: fitness(decode(c)), reverse=True)
    best = pop[0]
    print(f"Gen {g:02}:  {best}  =>  x={decode(best)},  f={fitness(decode(best))}")

    nextgen = [best]
    while len(nextgen) < pop_size:
        p1 = tournament(pop)
        p2 = tournament(pop)
        child = mutate(cross(p1, p2))
        nextgen.append(child)
    pop = nextgen

pop.sort(key=lambda c: fitness(decode(c)), reverse=True)
best = pop[0]

print("\nBest chromosome :", best)
print("Best x          :", decode(best))
print("Best fitness    :", fitness(decode(best)))
