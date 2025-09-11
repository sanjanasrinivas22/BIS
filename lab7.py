import random, math

def fitness(x):
    return x * math.sin(10 * math.pi * x) + 2

def init_pop(size):
    return [random.uniform(-1, 2) for _ in range(size)]

def select(pop, fits):
    total = sum(fits)
    r = random.uniform(0, total)
    cum = 0
    for p, f in zip(pop, fits):
        cum += f
        if cum >= r:
            return p
    return random.choice(pop)

def crossover(a, b, rate):
    if random.random() < rate:
        alpha = random.random()
        return alpha*a + (1-alpha)*b, alpha*b + (1-alpha)*a
    return a, b

def mutate(x, rate):
    if random.random() < rate:
        return random.uniform(-1, 2)
    return x

def run():
    POP, GEN = 6, 20
    CROSS, MUT = 0.8, 0.05
    pop = init_pop(POP)
    best, best_fit = None, float("-inf")

    for g in range(1, GEN+1):
        fits = [fitness(x) for x in pop]
        for x, f in zip(pop, fits):
            if f > best_fit:
                best, best_fit = x, f
        print(f"Gen {g}: Best Fitness = {best_fit:.4f}, x = {best:.4f}")

        new_pop = []
        while len(new_pop) < POP:
            p1, p2 = select(pop, fits), select(pop, fits)
            c1, c2 = crossover(p1, p2, CROSS)
            new_pop += [mutate(c1, MUT), mutate(c2, MUT)]
        pop = new_pop[:POP]

    print("\nBest solution found:")
    print(f"x = {best:.4f}")
    print(f"f(x) = {best_fit:.4f}")

if __name__ == "__main__":
    run()
