#Implement Greedy search algorithm for Kruskal's Minimal Spanning Tree Algorithm

# Function to find the minimum spanning tree using Kruskal's algorithm
def kruskal(graph):
    # Initialize variables
    mst = []
    parent = {}  # To track the parent node of each node
    rank = {}    # To track the rank of each node for union-find

    # Function to find the parent of a node using path compression
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])  # Path compression
        return parent[node]

    # Function to perform union of two sets
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            # Union by rank to optimize the depth of the tree
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    # Initialize parent and rank for each node
    for node in graph:
        parent[node] = node
        rank[node] = 0

    # Sort edges by weight
    edges = sorted((graph[node1][node2], node1, node2) for node1 in graph for node2 in graph[node1])

    # Iterate through sorted edges
    for weight, node1, node2 in edges:
        # Check if including this edge forms a cycle
        if find(node1) != find(node2):
            mst.append((node1, node2))
            union(node1, node2)

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
    mst = kruskal(graph)  # Find MST using Kruskal's algorithm
    display_mst(mst)      # Display the MST

# Execute main function
if __name__ == "__main__":
    main()
"""OUTPUT
A H 8
B C 8
B H 11
C D 7
C F 4
C I 2
H G 1
H I 7
D E 9
D F 14
I G 6
G F 2
F E 10
Minimum Spanning Tree:
G -- H
C -- I
F -- G
A -- B
C -- F
C -- D
A -- H
D -- E
=== Code Execution Successful ==="""