# kruskal-graph-and-mst-generator
Generates simple connected undirected graphs with random weight on each edge and one of their minimal spanning tree (MST) using Kruskal algorithm

# how it works
The script first create an edge for each vertex in this matter: 
- The vertex 0 is always connected to vertex 1 
- The an edge is create for each vertex from 0 to x (x being the last vertex) 
- The vertex x is connected to a random vertex from 0 to x-1 

This ensure that the graph is connected randomly (i'm not sure is purely random because vertex 1 is always connected to vertex 0, vertex 2 is always connected to 0 or 1, etc.)

The script then proceeds to add random vertices from a random vertex to another random vertex. If the connection already exist, or if the two random vertices are the same (ex: randomly picking vertex 3 twice) the script tries again. After NUMBER_OF_TRIES (default to 100) tries, the script fails an returns a partially created graph. Each time an edges is created the number of tries resets. 

At the end, the script creates two files. One files, `graph.data` with the graph created with each edge value as `{from_edge, to_edge, weight}`. The other file, `mst.data`, is created only if the graph is successfully created. 

# note
There can be multiple MST to a graph. The script only provides one MST, so it might no be the only output when using the Kruskal's algorithm