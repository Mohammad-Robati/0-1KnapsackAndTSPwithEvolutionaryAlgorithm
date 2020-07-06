from geneticAlgorithm import GenerationAlgorithm
from random import shuffle, randint
import math
import matplotlib.pyplot as plt


class TravellingSalesmanProblem(GenerationAlgorithm):

    def __init__(self, goodPaths, items, populationSize, tournumentSize, mutationRate, numberOfGenerations):
        super().__init__(items, populationSize, tournumentSize, mutationRate, numberOfGenerations)
        self.goodPaths = goodPaths

    def makeInitialPopulation(self):
        if self.goodPaths != None:
            return self.goodPaths
        populationSize = self.populationSize
        numberOfItems = len(self.items)
        population = []
        for i in range(populationSize):
            chromosome = [j+1 for j in range(numberOfItems)]
            shuffle(chromosome)
            population.append(chromosome)
        return population

    def getDistance(self, point1, point2):
        return math.sqrt(math.pow(point2["x"]-point1["x"], 2) + math.pow(point2["y"]-point1["y"], 2))

    def getFitness(self, chromosome):
        items = self.items
        sum = 0
        for i in range(len(chromosome) - 1):
            sum += self.getDistance(items[chromosome[i]-1], items[chromosome[i+1]-1])
        return -sum

    def runTournument(self, population):
        return super().runTournument(population)

    def crossOver(self, parents):
        childs = []
        items = self.items
        while len(childs) < self.populationSize:
            father = parents[randint(0, len(parents) - 1)]
            mother = parents[randint(0, len(parents) - 1)]
            pivot1 = randint(0, int(len(father)/2 - 1))
            pivot2 = randint(int(len(father)/2), len(father) - 1)
            staticPartition = mother[pivot1:pivot2]
            child1 = [0 for i in range(len(father))]
            child1[pivot1:pivot2] = staticPartition
            currFather = pivot2
            currMother = pivot2
            while currMother != pivot1:
                if father[currFather] not in staticPartition:
                    child1[currMother] = father[currFather]
                    currMother = (currMother + 1) % len(mother)
                currFather = (currFather + 1) % len(father)
            staticPartition = father[pivot1:pivot2]
            child2 = [0 for i in range(len(father))]
            child2[pivot1:pivot2] = staticPartition
            currFather = pivot2
            currMother = pivot2
            while currFather != pivot1:
                if mother[currMother] not in staticPartition:
                    child2[currFather] = mother[currMother]
                    currFather = (currFather + 1) % len(father)
                currMother = (currMother + 1) % len(mother)
            childs.append(child1)
            childs.append(child2)
        return childs

    def mutate(self, childs):
        mutatedGenomes = int(len(childs) * self.mutationRate)
        while mutatedGenomes != 0:
            chromosome = randint(0, len(childs) - 1)
            point1 = randint(0, len(childs[0]) - 1)
            point2 = randint(0, len(childs[0]) - 1)
            tmp = childs[chromosome][point1]
            childs[chromosome][point1] = childs[chromosome][point2]
            childs[chromosome][point2] = tmp
            mutatedGenomes -= 1
        return childs

    def getFitnessForWholeGeneration(self, generation):
        return super().getFitnessForWholeGeneration(generation)

    def runGeneticAlgorithm(self):
        return super().runGeneticAlgorithm()

    def run(self):
        generations = self.runGeneticAlgorithm()
        for g in generations:
            print(-g[2])
        self.plot(generations[len(generations)-1][3])

    def plot(self, answer):
        items = self.items
        x, y = [], []
        for point in answer:
            x.append(items[point-1]["x"])
            y.append(items[point-1]["y"])
        plt.plot(x, y, '-o')
        plt.show()





