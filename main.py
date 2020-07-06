from knapsackProblem import KnapsackProblem
from tspProblem import TravellingSalesmanProblem
from nearest_neighbor_tour import NearestNeighborTour
from graph import Graph

tab = 1

if tab == 0:

    # 1 ==> 9147
    # 2 ==> 1514
    # 3 ==> 2397
    file = open("./inputs/knapsack_2.txt", "r")
    numberOfItems, capacity = file.readline().split(" ")
    numberOfItems = int(numberOfItems)
    capacity = int(capacity)
    items = []
    index = 0
    for line in file:
        value = int(line.split(" ")[0])
        weight = int(line.split(" ")[1])
        items.append({"value": value, "weight": weight, "index": index})
        index += 1
    kp = KnapsackProblem(capacity,
                         items=items,
                         populationSize=1000,
                         tournumentSize=100,
                         mutationRate=1,
                         numberOfGenerations=100)
    kp.run()

else:

    items = []
    points = []
    file = open("./inputs/tsp_data.txt", "r")
    for line in file:
        index, x, y = line.split(" ")
        index = int(index)
        point = []
        x = float(x)
        y = float(y)
        point.append(x)
        point.append(y)
        points.append(point)
        items.append({"index": index, "x": x, "y": y})

    withHeurisitic = True
    goodPaths = None
    populationSize = 1000
    if withHeurisitic:
        graph = Graph(points)
        goodPaths = NearestNeighborTour(graph.get_adjacent_matrix(), 0).getGoodPaths(populationSize)
        tsp = TravellingSalesmanProblem(
            goodPaths=goodPaths,
            items=items,
            populationSize=populationSize,
            tournumentSize=100,
            mutationRate=1,
            numberOfGenerations=1000)
        tsp.run()
    else:
        tsp = TravellingSalesmanProblem(
            goodPaths=goodPaths,
            items=items,
            populationSize=500,
            tournumentSize=50,
            mutationRate=1,
            numberOfGenerations=500)
        tsp.run()

