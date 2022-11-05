import random
from collections import namedtuple


N = 20
POPULATION_SIZE = N * 5
OFFSPRING_SIZE = N * 2
NUM_GENERATIONS = N * 50

Individual = namedtuple('Individual', ['genome', 'missing', 'weight'])


def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]


def computeFitness(indices: list):
    global N, myLists, goal
    currentLists = [l for i, l in enumerate(myLists) if indices[i]]
    weight = sum(len(l) for l in currentLists)
    available = set(element for sublist in currentLists for element in sublist)
    missing = N - sum(element in available for element in goal)
    return missing, weight


def tournament(population, tournament_size=2):
    return min(random.choices(population, k=tournament_size), key=lambda i: (i.missing, i.weight))

def crossOver(genome1, genome2):
    cut = random.randint(0, len(genome1))
    return genome1[:cut] + genome2[cut:]

def mutation(genome):
    point = random.randint(0, len(genome) - 1)
    return genome[:point] + [not genome[point]] + genome[point + 1 :]

if __name__ == '__main__':
    
    

    myLists = problem(N, 42)
    goal = set(range(N))
    population = list()

    for genome in [[random.choice([True, False]) for _ in myLists] for _ in range(POPULATION_SIZE)]:
        fitness = computeFitness(genome)
        population.append(Individual(genome, fitness[0], fitness[1]))
    
    

    for g in range(NUM_GENERATIONS):
        offspring = list()
        for i in range(OFFSPRING_SIZE):
            p = tournament(population)
            o = mutation(p.genome)
            f = computeFitness(o)
            
            offspring.append(Individual(o, f[0], f[1]))
        population += offspring
        population = sorted(population, key=lambda i: (i.missing, i.weight))[:POPULATION_SIZE]

    

    solution = population[0]
    print(f'Missing: {solution.missing}, Solution: {solution.weight}')