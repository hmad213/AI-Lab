import random
import math

cost_matrix = [
    [4, 6, 8, 7, 5],
    [7, 5, 6, 8, 4],
    [6, 4, 7, 5, 8],
    [5, 8, 6, 4, 7],
    [8, 6, 5, 7, 4],
    [7, 4, 8, 6, 5],
    [6, 7, 4, 5, 8],
    [5, 6, 7, 8, 4],
    [4, 7, 5, 6, 8],
    [8, 5, 6, 4, 7]
]

def calculate_fitness(individual: list):
    total_cost = 0
    for i in range(len(individual)):
        total_cost += cost_matrix[i][individual[i]]
    return 1 / total_cost

def create_random_individual():
    return [random.randint(0, 4) for _ in range(10)]

def select_parents(population: list[list], fitness_scores: list[int]):
    sorted_board = [board for board, _ in sorted(zip(population, fitness_scores), reverse=True)]
    return sorted_board[:math.floor(len(population) / 2)]

def crossover(parent1: list, parent2: list):
    point = random.randint(1, len(parent1) - 2)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(individual: list):
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

def genetic(size: int, generations: int):
    population_size = size
    population = [create_random_individual() for _ in range(population_size)]
    best_fitness = 0
    for i in range(generations):
        fitness_scores = [calculate_fitness(population[i]) for i in range(len(population))]
        best_fitness = max(fitness_scores)

        parents = select_parents(population, fitness_scores)

        new_population = []
        for i in range(population_size):
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            new_population.append(child)

        mutation_rate = 0.1
        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                population[i] = mutate(new_population[i])

        population = new_population

    best_individual = max(population, key=calculate_fitness)
    return best_individual, calculate_fitness(best_individual)

print(genetic(10, 100))
print(genetic(30, 100))