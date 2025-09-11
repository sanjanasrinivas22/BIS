import random

POP = 6
BITS = 5
GEN = 5
CROSS = 0.7
MUT = 0.1

def fit(s):
    return int(s, 2) ** 2

def init_pop():
    return [''.join(random.choice('01') for _ in range(BITS)) for _ in range(POP)]

def select(p):
    a, b = random.sample(p, 2)
    return a if fit(a) > fit(b) else b

def cross(a, b):
    if random.random() < CROSS:
        pt = random.randint(1, BITS - 1)
        return a[:pt] + b[pt:], b[:pt] + a[pt:]
    return a, b

def mutate(s):
    return ''.join('1' if c == '0' and random.random() < MUT else
                   '0' if c == '1' and random.random() < MUT else c
                   for c in s)

def run():
    pop = init_pop()
    best, best_fit = None, -1
    for g in range(1, GEN + 1):
        for x in pop:
            f = fit(x)
            if f > best_fit:
                best, best_fit = x, f
        print(f"Gen {g}: {best} (x={int(best,2)}), Fit={best_fit}")
        nxt = []
        while len(nxt) < POP:
            p1, p2 = select(pop), select(pop)
            c1, c2 = cross(p1, p2)
            nxt.extend([mutate(c1), mutate(c2)])
        pop = nxt[:POP]
    print(f"\nBest: {best} (x={int(best,2)}), Fit={best_fit}")

if __name__ == "__main__":
    run()
