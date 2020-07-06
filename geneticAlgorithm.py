import sys
from random import randint
from math import inf
from copy import deepcopy


class GenerationAlgorithm:

    def __init__(self, items, populationSize, tournumentSize, mutationRate, numberOfGenerations):
        self.items = items
        self.populationSize = populationSize
        self.tournumentSize = tournumentSize
        self.mutationRate = mutationRate
        self.numberOfGenerations = numberOfGenerations

    def makeInitialPopulation(self):
        pass

    def getFitness(self, chromosome):
        pass

    def runTournument(self, population):
        populationSize = self.populationSize
        tournumentSize = self.tournumentSize
        chromosomes = deepcopy(population)
        parents = []
        for i in range(int(populationSize / tournumentSize)):
            participants = []
            for i in range(tournumentSize):
                if len(chromosomes) - 1 > 0:
                    participants.append(chromosomes.pop(randint(0, len(chromosomes) - 1)))
            max = -inf
            best = -1
            for i in range(0, len(participants) - 1):
                fitnessValue = self.getFitness(participants[i])
                if fitnessValue > max:
                    max = fitnessValue
                    best = i
            parents.append(participants[best])
        return parents

    def crossOver(self, parents):
        pass

    def mutate(self, childs):
        pass

    def getFitnessForWholeGeneration(self, generation):
        min = inf
        max = -inf
        sum = 0
        answer = None
        for chromosome in generation:
            chromosomeValue = self.getFitness(chromosome)
            if chromosomeValue > max:
                max = chromosomeValue
                answer = chromosome
            if chromosomeValue < min:
                min = chromosomeValue
            sum += chromosomeValue
        avg = sum / len(generation)
        return min, avg, max, answer

    def runGeneticAlgorithm(self):
        numberOfGenerations = self.numberOfGenerations
        generations = []
        initialGeneration = self.makeInitialPopulation()
        generations.append(self.getFitnessForWholeGeneration(initialGeneration))
        for i in range(numberOfGenerations):
            print('Generation #', i)
            newGeneration = self.mutate(self.crossOver(self.runTournument(initialGeneration)))
            generations.append(self.getFitnessForWholeGeneration(newGeneration))
            initialGeneration = newGeneration
        return generations

