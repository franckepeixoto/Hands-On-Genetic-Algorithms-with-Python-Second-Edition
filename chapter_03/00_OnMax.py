from deap import creator,tools,base
import numpy as np
import random

# Genetic Algorithm constants:
POPULATION_SIZE = 200
 # set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

class Employee:
    def __init__(self):
        self.type  = ""
class Dev(Employee):
    def __init__(self):
        self.programmingLanguages = set()

toolbox = base.Toolbox() 

creator.create("Dev",Employee,type="Dev",programmingLanguages=set)
creator.create("FitMax",base.Fitness,weights=(1.0,))
creator.create("FitMin",base.Fitness,weights=(-1.0,))
creator.create("FitCompound",base.Fitness,weights=(1.0,0.2,-0.4))
creator.create("Individual",list, fitness=creator.FitMax)

def soma(a,b):
    return a+b
toolbox.register("soma",soma,b=3)

def zeroOrOne():
    return random.randint(0,1)

randomList = tools.initRepeat(list,zeroOrOne,30)


print(randomList)
# create the individual operator to fill up an Individual instance:
#toolbox.register("Dev", creator.Dev, toolbox.)

#population = toolbox.populationCreator(n=POPULATION_SIZE)
#generationCounter = 0

#print(population)

#fitnessValues = list(map(toolbox.evaluate, population))
#print(fitnessValues)
# calculate fitness tuple for each individual in the population:
