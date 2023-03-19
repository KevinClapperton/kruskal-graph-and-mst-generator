import random
# Kruskal's algorithm in Python

# Most of the code is taken from https://www.programiz.com/dsa/kruskal-algorithm

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self._graph = []
        self._edge_index = 0
        self._number_of_edges = 0

    def add_edge(self, edge):
        self._graph.append(edge)
        self._number_of_edges = self._number_of_edges + 1

    def __iter__(self):
        return self 

    def __next__(self):
        if self._edge_index < (self._number_of_edges - 1):            
            self._edge_index += 1
            return self._graph[self._edge_index]        
        raise StopIteration

    def __getitem__(self, idx): 
        return self._graph[idx]

class Kruskal:
    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def run(self, graph):
        result = []
        i, e = 0, 0
        graphSortedList = sorted(graph, key=lambda item: item[2])
        graph._graph = graphSortedList
        parent = []
        rank = []
        for node in range(graph.V):
            parent.append(node)
            rank.append(0)
        while e < graph.V - 1:
            u, v, w = graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        # Making resulted graph 
        resultGraph = Graph(graph.V)
        for edge in range(len(result)): 
            resultGraph.add_edge(result[edge])

        return resultGraph

def createFileFromGraph(name, graph: Graph): 
    fp = open(name, 'w')
    for edge in graph._graph:  
        fp.write("{{{}, {}, {}}},\n".format(edge[0], edge[1], edge[2]))
    # deleting the two last char
    fp.seek(0,2)
    size=fp.tell()
    fp.truncate(size-3)
    fp.close()

def createRandomGraph(nVertices, nEdges, maxWeight): 
    # make sure nEdges is reasonable
    maxNEdges = nVertices*(nVertices - 1)/2
    if nEdges > maxNEdges: 
        return None

    # make a connected non-complete graph with nVertices-1 edges 
    newGraph = []
    
    for v in range(nVertices):  
        if (v > 0): 
            newGraph.append([v, random.randrange(v)])

    # Make random connections until there is nEdges
    maxNTries = 100
    nTries = 0
    while(len(newGraph) < nEdges): 
        u = random.randrange(nVertices)
        v = random.randrange(nVertices)

        if u == v: 
            nTries += 1
            continue 
        if [u, v] in newGraph or [v, u] in newGraph: 
            nTries += 1
            continue
        if nTries >= maxNTries: 
            return None # failed to create graph 

        newGraph.append([u, v])

    #creating Graph instance 
    g = Graph(nVertices)
    g._number_of_edges = nEdges 

    for edge in newGraph: 
        edge.append(random.randrange(maxWeight) + 1)
        g._graph.append(edge)

    return g

g = createRandomGraph(5, 9, 10)
createFileFromGraph("graph.data", g)

algo = Kruskal() 
newG = algo.run(g)

createFileFromGraph("mst.data", newG)