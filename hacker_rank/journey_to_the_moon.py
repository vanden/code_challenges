# https://www.hackerrank.com/challenges/journey-to-the-moon/problem

from collections import defaultdict


def journeyToMoonSlow(n, astronauts):
    # Times out on case 11
    counts = getCountryCounts(n, astronauts)
    pairCount = 0
    for i, v in enumerate(counts):
        for _, u in enumerate(counts[i+1:]):
            pairCount += v * u
    return pairCount

def getCountryCounts(n, astronauts):
    nodes = []
    classes = defaultdict(set)
    for i in range(n):
        nodes.append(Node(i))

    for first, second in astronauts:
        nodes[first].addEdge(second)
        nodes[second].addEdge(first)

    queue = []
    for i in range(n):
        if not nodes[i].explored:
            classes[i].add(i)
            queue.append(nodes[i])
            nodes[i].explored = True
            while queue:
                current = queue.pop()
                current.explored = True
                for edge in current.edges:
                    if not nodes[edge].explored:
                        queue.append(nodes[edge])
                        classes[i].add(edge)
    counts = [len(s) for s in classes.values()]

    return counts

class Node():
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.explored = False
    def addEdge(self, toIndex):
        self.edges.append(toIndex)
    def __repr__(self):
        return "Node(%s) with edges: %s and Explored: %s" %(
            self.index, self.edges, self.explored)

################################################################

def journeyToMoon(n, astronauts):
    pass
