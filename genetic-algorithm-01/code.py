import random
import string

def fitness(individual, objective):
    return sum(1 for a, b in zip(individual, objective) if a == b)


def new_individual(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
    

def mutation(individual):
    individual = list(individual)
    changes = max(1, len(individual) // 5)
    for _ in range(changes):
        idx = random.choice(range(len(individual)))
        individual[idx] = random.choice(string.printable)
    return ''.join(individual)


def crossover(ind1, ind2):
    breakpoint = random.choice(range(len(ind1)))
    return ind1[breakpoint:] + ind2[:breakpoint]

def genetic_algorithm(objective, individuals, generations):

    if generations == 0: 
        return individuals
    
    individuals = sorted(individuals, key=lambda x: x[1], reverse=True)

    num_survivors = len(individuals)//4 

    survivors = individuals[num_survivors:]

    for i in range(num_survivors, len(individuals)):
        child = crossover(
            ind1 = survivors[random.randint(0, num_survivors-1)][0],
            ind2 = survivors[random.randint(0, num_survivors-1)][0]
        )
        individuals[i] = (child, fitness(child, objective))
        
     
    for i in range(num_survivors):
        new_mutation = mutation(survivors[i][0])
        fit_mutation = fitness(individual=new_mutation, objective=objective)
        if individuals[i][1] < fit_mutation: 
            individuals[i] = (new_mutation, fit_mutation)

    print(survivors[0][0])

    individuals = genetic_algorithm(objective=objective, individuals=individuals, generations=generations-1)
    return individuals


def execute(objective, generations):

    individuals = []

    for i in range(800):
        individual = new_individual(length=len(objective))
        individuals.append((individual, fitness(individual, objective)))

    new_individuals = genetic_algorithm(objective=objective, individuals=individuals, generations=generations)

    print("Best child: ", sorted(new_individuals, key=lambda x: x[1], reverse=True)[0])


execute(input(), 800)


          
