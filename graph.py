import math


class Graph:

    def __init__(self, points):
        self.points = points

    def get_adjacent_matrix(self):
        points = self.points
        edges = []
        for i in range(0, len(points)):
            list = []
            for j in range(0, len(points)):
                dist = math.sqrt(pow(points[i][0] - points[j][0], 2)
                                 + pow(points[i][1] - points[j][1], 2))
                list.append(dist)
            edges.append(list)
        return edges
