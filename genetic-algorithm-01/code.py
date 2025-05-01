import random
import string

OBJETIVE = "Hello World!"
GENERATIONS = 50

def fitness(individual):
    potential = 0
    for i in range(1, len(individual)):
        if individual[i-1] == OBJETIVE[i-1]:
            potential += 1
    return potential

def new_individual():
    individual = ""
    for i in range(1, len(individual)):
        individual.append(random.choice(string.printable))
    return individual

def mutation(individual):
    changes = len(individual)//10
    for i in range(1, changes):
        individual[random.randint(0, len(individual)-1)] = random.choice(string.printable)
    return individual

def crossover(ind1, ind2):
    breakpoint = random.randint(0, len(OBJETIVE))
    return ind1[breakpoint:] + ind2[:breakpoint]

ndef genetic_algorithm():
    generation = []
    fitnesses = []
    for i in range(1, 20):
        individual = new_individual()
        generation.append((individual, fitness(individual)))
    
    

          
