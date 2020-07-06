from geneticAlgorithm import GenerationAlgorithm
from random import randint
from copy import deepcopy
import matplotlib.pyplot as plt


class KnapsackProblem(GenerationAlgorithm):

    def __init__(self, capacity, items, populationSize, tournumentSize, mutationRate, numberOfGenerations):
        super().__init__(items, populationSize, tournumentSize, mutationRate, numberOfGenerations)
        self.capacity = capacity

    def makeInitialPopulation(self):
        populationSize = self.populationSize
        numberOfItems = len(self.items)
        population = []
        for i in range(populationSize):
            chromosome = [0 for i in range(numberOfItems)]
            items = deepcopy(self.items)
            for j in range(numberOfItems):
                if len(items) != 1:
                    index = randint(0, len(items)-1)
                else:
                    index = 0
                item = items.pop(index)
                isTaken = randint(0, 1)
                if isTaken == 1:
                    chromosome[item['index']] = 1
                    self.getFitness(chromosome)
            population.append(chromosome)
        return population

    def getFitness(self, chromosome):
        items = self.items
        totalValue = 0
        totalWeight = 0
        index = 0
        ones = []
        for gene in chromosome:
            if gene == 1:
                ones.append(index)
                totalValue += items[index]['value']
                totalWeight += items[index]['weight']
            index += 1
        while totalWeight > self.capacity:
            index = chromosome.index(1)
            chromosome[index] = 0
            totalWeight -= items[index]['weight']
        return totalValue

    def runTournument(self, population):
        return super().runTournument(population)

    def crossOver(self, parents):
        childs = []
        items = self.items
        while len(childs) < self.populationSize:
            father = parents[randint(0, len(parents) - 1)]  # :D
            mother = parents[randint(0, len(parents) - 1)]
            takenIndices = []
            for i in range(len(father)):
                if father[i] == 1:
                    takenIndices.append(i)
                elif mother[i] == 1:
                    takenIndices.append(i)
            chromosomes = [0 for p in range(len(father))]
            currWeight = 0
            while len(takenIndices) != 0:
                index = takenIndices.pop(0)
                currWeight += items[index]['weight']
                if currWeight > self.capacity:
                    break
                chromosomes[index] = 1
            childs.append(chromosomes)
        return childs

    def mutate(self, childs):
        mutatedGenomes = int(len(childs) * self.mutationRate)
        while mutatedGenomes != 0:
            chromosomeIndex = randint(0, len(childs) - 1)
            geneIndex = randint(0, len(childs[0]) - 1)
            childs[chromosomeIndex][geneIndex] = 1 - childs[chromosomeIndex][geneIndex]
            self.getFitness(childs[chromosomeIndex])
            mutatedGenomes -= 1
        return childs

    def getFitnessForWholeGeneration(self, generation):
        return super().getFitnessForWholeGeneration(generation)

    def runGeneticAlgorithm(self):
        return super().runGeneticAlgorithm()

    def run(self):
        generations = self.runGeneticAlgorithm()
        for g in generations:
            print(g[2])
        self.plot(generations)

    def plot(self, generations):
        x = ['min', 'avg', 'max']
        y1 = generations[0][0:3]
        y2 = generations[len(generations)-1][0:3]
        plt.plot(x, y1, '-o')
        plt.plot(x, y2, '-o')
        plt.show()






