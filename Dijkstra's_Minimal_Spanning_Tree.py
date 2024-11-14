#Implement Greedy search algorithm for Dijkstra's Minimal Spanning Tree Algorithm
import heapq

# Function to find the shortest path from source node to all other nodes using Dijkstra's algorithm
def dijkstra(graph, source):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Priority queue to store nodes with their distances
    pq = [(0, source)]

    # Dijkstra's algorithm
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if the current distance is greater than the already calculated distance
        if current_distance > distances[current_node]:
            continue

        # Update distances to neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

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

# Function to display the shortest path distances
def display_shortest_paths(distances):
    print("Shortest path distances from the source node:")
    for node, distance in distances.items():
        print("Node:", node, "Distance:", distance)

# Main function
def main():
    graph = input_graph()   # Input the graph
    source = input("Enter the source node: ")  # Input the source node
    distances = dijkstra(graph, source)  # Find shortest paths using Dijkstra's algorithm
    display_shortest_paths(distances)   # Display the shortest paths

# Execute main function
if __name__ == "__main__":
    main()
"""OUTPUT
Enter the number of edges in the graph: 14
Enter the edges and weights (node1 node2 weight) one per line:
a b 4
a h 8
b c 8
c d 7
c f 4
c i 2
h g 1
h i 7
d e 9
d f 14
i g 6
g f 2
f e 10
b h 11
Enter the source node: e
Shortest path distances from the source node:
Node: a Distance: 21
Node: b Distance: 22
Node: h Distance: 13
Node: c Distance: 14
Node: d Distance: 9
Node: f Distance: 10
Node: i Distance: 16
Node: g Distance: 12
Node: e Distance: 0
=== Code Execution Successful ==="""