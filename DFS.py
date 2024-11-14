#DFS
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
    return visited

def main():
    graph = {}
    num_edges = int(input("Enter the number of edges in the graph: "))
    print("Enter the graph edges (node1 node2) one per line:")
    for _ in range(num_edges):
        node1, node2 = input().split()
        graph.setdefault(node1, []).append(node2)
        graph.setdefault(node2, []).append(node1)

    start_node = input("Enter the starting node for DFS: ")
    visited_nodes = dfs(graph, start_node, [])

    print("Depth-First Search:")
    print(visited_nodes)

if __name__ == "__main__":
    main()
"""OUTPUT
Enter the number of edges in the graph: 5
Enter the graph edges (node1 node2) one per line:
0 1
0 2 
0 3
2 3 
2 4
Enter the starting node for DFS: 0
Depth-First Search:
['0', '1', '2', '3', '4']
=== Code Execution Successful ==="""