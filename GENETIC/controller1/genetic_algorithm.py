

DNA_SIZE = 8
POPULATION_SIZE = 20
NUM_PARENTS = POPULATION_SIZE // 5
GENERATIONS = 30
MUTATION_RATE = 0.1
AMPLITUDE_DNA = 100
import random
import math



    
def RandomPopulation():
    """Devolve um individuo aleatorio"""
    population = []
    for x in range(0, POPULATION_SIZE):
        population.append(random.sample(range(AMPLITUDE_DNA), DNA_SIZE))
    return population

def Crossover(father, mother):
    """Devolve uma tupla com os dois filhos gerados entre um pai e uma mae
    
            Herda de forma aleatoria de cada pai, indice a indice"""
    
    children1 = []
    children2 = []
    for x in range(0, DNA_SIZE):
        r = random.randint(0, 1)
        if r:
            children1.append(father[x])
            children2.append(mother[x])
        else:
            children1.append(mother[x])
            children2.append(father[x])

    return (children1, children2)


def CrossoverPopulation(population):
    """Recebe uma populacao soh com os pais e devolve preenchida com filhos
    
        Vai selecionando pais aleatorios e preenchendo a populacao"""

    numParents = len(population)
    numChildrens = POPULATION_SIZE - numParents # o espaço que sobra
        
    for x in range(math.ceil(numChildrens/2)):
        father = random.randint(0, numParents -1)
        mother = random.randint(0, numParents -1)
        
        while(mother == father):  
            mother = random.randint(0, numParents-1)

        population += list(Crossover(population[father], population[mother]))
    if((numChildrens % 2 )!= 0):
        population = population[:-1]


    return population

def Mutation(individual):
    """Devolve o individuo apos o processo de mutacao
    
        Pra cada indice, tem a probabilidade de mutar(calcular um novo valor aleatorio)"""
    for  x in range(DNA_SIZE):
        if random.random() < MUTATION_RATE:
            individual[x] = random.randint(0, AMPLITUDE_DNA)
    return individual

def MutationPopulation(population):
    """ Devolve uma populacao apos passar todos os filhos pelo processo de mutacao"""
    mutatedPopulation = population[:NUM_PARENTS] 

    for x in population[NUM_PARENTS:]:
        mutatedPopulation.append(Mutation(x))

    return mutatedPopulation

def FitnessPopulation(population,controller,g):
    """Avalia uma populacao inteira e devolve uma lista com elas na mesma ordem"""
    populationScore = []
    for x in range(0, POPULATION_SIZE):
        fit = controller.run_episode(population[x])
        populationScore.append((population[x],fit))

    return populationScore

def GeneticSolution(controller):
    # Populaçao inicial aleatoria
    population = RandomPopulation()
    

        
    for g in range(0,GENERATIONS):
        # populaçao avalia
            
        pop_score = FitnessPopulation(population,controller,g)
            
        # Seleçao
        pop_score_sel = sorted(pop_score,reverse = True, key=lambda tup: tup[1])
            
            
        population = []
        for x in range(NUM_PARENTS):
            population.append(pop_score_sel[x][0])
        # descendentes
        
        population = CrossoverPopulation(population)
        population = MutationPopulation(population)
        print(g)
            


    print(population[0])
        

    return population[0]



