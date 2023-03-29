import random
import time
import math
# Kruskal's algorithm in Python

# Most of the code is taken from https://www.programiz.com/dsa/kruskal-algorithm

NUMBER_OF_VERTICES = 500
NUMBER_OF_EDGES = 50000
MAX_WEIGHT = 10000

NUMBER_OF_TRIES = 100

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

    def partition(self, graph, beg, end): 
        p=beg
        pivot=graph[end][2] # getting last weight as pivot
        for i in range(beg, end):
            if graph[i][2]<=pivot:
                graph._graph[i], graph._graph[p] = graph._graph[p], graph._graph[i]
                p += 1
        graph._graph[end], graph._graph[p] = graph._graph[p], graph._graph[end]
        return p

    def quicksort(self, graph, beg, end): 
        # Code adapted from https://stackoverflow.com/a/68553264/10919275
        # Create an auxiliary stack
        size = end - beg + 1
        stack = [0] * (size)
    
        # initialize top of stack
        top = -1
    
        # push initial values of beg and end to stack
        top = top + 1
        stack[top] = beg
        top = top + 1
        stack[top] = end
    
        # Keep popping from stack while is not empty
        while top >= 0:
    
            # Pop end and beg
            end = stack[top]
            top = top - 1
            beg = stack[top]
            top = top - 1
    
            # Set pivot element at its correct position in
            # sorted array
            p = self.partition( graph, beg, end )
    
            # If there are elements on right side of pivot,
            # then push right side to stack
            if p+1 < end:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = end

            # If there are elements on left side of pivot,
            # then push left side to stack
            if p-1 > beg:
                top = top + 1
                stack[top] = beg
                top = top + 1
                stack[top] = p - 1
        



    #  Applying Kruskal algorithm
    def run(self, graph):
        result = []
        i, e = 0, 0
        self.quicksort(graph, 0, len(graph._graph) - 1)
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
    maxNTries = NUMBER_OF_TRIES
    nTries = 0
    current_time = math.floor(time.time())
    while(len(newGraph) < nEdges): 
        u = random.randrange(nVertices)
        v = random.randrange(nVertices)

        if current_time != math.floor(time.time()):  
            current_time = math.floor(time.time())
            print("Number of edges created: " + str(len(newGraph)))
        if u == v: 
            nTries += 1
            continue 
        if [u, v] in newGraph or [v, u] in newGraph: 
            nTries += 1
            continue
        if nTries >= maxNTries: 
            print("Failed to complete graph")
            print("Number of tries to add a random edge: " + str(maxNTries))
            break  # failed to create graph 
        
        nTries = 0
        newGraph.append([u, v])

    #creating Graph instance 
    g = Graph(nVertices)
    g._number_of_edges = nEdges 

    for edge in newGraph: 
        edge.append(random.randrange(maxWeight) + 1)
        g._graph.append(edge)

    return g

if __name__ == "__main__":
    for i in range(5): 
        g = createRandomGraph(NUMBER_OF_VERTICES, NUMBER_OF_EDGES, MAX_WEIGHT)

        createFileFromGraph("graph" + str(i) + ".data", g)

        if len(g._graph) < NUMBER_OF_EDGES: # The script failed to create the graph with NUMBER_OF_EDGES
            exit()

        algo = Kruskal() 
        newG = algo.run(g)

        createFileFromGraph("mst" + str(i) + ".data", newG)