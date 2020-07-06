import random
from copy import deepcopy

class NearestNeighborTour:

    def __init__(self, adjacent_matrix, start_point):
        self.adjacent_matrix = adjacent_matrix
        self.start_point = start_point

    def run_algorithm(self):
        adjacent_matrix = self.adjacent_matrix
        unvisited_points = []
        path = []
        cost = 0
        n = len(adjacent_matrix[0])
        for i in range(0, n):
            unvisited_points.append(i)
        current_point = unvisited_points.pop(self.start_point)
        path.append(self.start_point + 1)
        while len(unvisited_points) != 0:
            tmp_array = []
            for j in range(0, len(unvisited_points)):
                tmp_array.append([adjacent_matrix[current_point][unvisited_points[j]],
                                  unvisited_points[j]])
            min_dist = min(tmp_array)
            cost += min_dist[0]
            current_point = unvisited_points.pop(unvisited_points.index(min_dist[1]))
            path.append(min_dist[1] + 1)
        cost += adjacent_matrix[path[n-1]][self.start_point]
        path.append(self.start_point)
        return path

    def swap_random(self, list):
        seq = deepcopy(list)
        pivot1 = random.randint(1, len(list)-1)
        pivot2 = random.randint(1, len(list)-1)
        tmp = deepcopy(seq[min(pivot1, pivot2):max(pivot1, pivot2)])
        random.shuffle(tmp)
        seq[min(pivot1, pivot2):max(pivot1, pivot2)] = tmp
        return seq

    def getGoodPaths(self, numberOfPaths):
        goodPaths = []
        path = self.run_algorithm()
        goodPaths.append(path)
        for i in range(numberOfPaths-1):
            newPath = self.swap_random(path)
            goodPaths.append(newPath)
        return goodPaths








