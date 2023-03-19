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


g = Graph(6)

g.add_edge([0, 1, 4])
g.add_edge([0, 2, 4])
g.add_edge([1, 2, 2])
g.add_edge([2, 3, 3])
g.add_edge([2, 5, 2])
g.add_edge([2, 4, 4])
g.add_edge([3, 4, 3])
g.add_edge([5, 4, 3])

algo = Kruskal() 
newG = algo.run(g)

print(newG._graph)