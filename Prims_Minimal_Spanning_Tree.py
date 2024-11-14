#Implement Greedy search algorithm for Prim's Minimal Spanning Tree Algorithm
# Function to find the minimum spanning tree using Prim's algorithm
def prim(graph):
    # Initialize variables
    mst = []
    visited = set()
    start_node = next(iter(graph))  # Start from any node

    # Add the start node to the visited set
    visited.add(start_node)

    # Loop until all nodes are visited
    while len(visited) < len(graph):
        min_edge = None
        min_weight = float('inf')

        # Iterate through visited nodes
        for node in visited:
            # Check adjacent nodes
            for neighbor, weight in graph[node].items():
                # If neighbor is not visited and the weight is less than the minimum weight
                if neighbor not in visited and weight < min_weight:
                    # Update minimum weight and edge
                    min_weight = weight
                    min_edge = (node, neighbor)

        # Add the minimum weight edge to the MST
        if min_edge:
            mst.append(min_edge)
            # Add the new node to visited set
            visited.add(min_edge[1])

    return mst

# Function to take input for the graph
def input_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges in the graph: "))
    print("Enter the edges and weights (node1 node2 weight) one per line:")
    for _ in range(num_edges):
        node1, node2, weight = input().split()
        weight = int(weight)
        # Add edges to the graph (undirected graph)
        graph.setdefault(node1, {})[node2] = weight
        graph.setdefault(node2, {})[node1] = weight
    return graph

# Function to display the Minimum Spanning Tree
def display_mst(mst):
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge[0], "--", edge[1])

# Main function
def main():
    graph = input_graph()  # Input the graph
    mst = prim(graph)      # Find MST using Prim's algorithm
    display_mst(mst)       # Display the MST

# Execute main function
if __name__ == "__main__":
    main()

"""OUTPUT
    Enter the number of edges in the graph: 14
Enter the edges and weights (node1 node2 weight) one per line:
a b 4
a h 8
b h 11
b c 8 
c d 7
c i 2
c f 4
h i 7
h g 1
d e 9
d f 14
i g 6
g f 2
f e 10
Minimum Spanning Tree:
a -- b
b -- c
c -- i
c -- f
f -- g
g -- h
c -- d
d -- e
=== Code Execution Successful ==="""