#BFS
def bfs(graph, queue, visited):
    if not queue:
        return visited
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return bfs(graph, queue, visited)

def main():
    graph = {}
    num_edges = int(input("Enter the number of edges in the graph: "))
    print("Enter the graph edges (node1 node2) one per line:")
    for _ in range(num_edges):
        node1, node2 = input().split()
        graph.setdefault(node1, []).append(node2)
        graph.setdefault(node2, []).append(node1)

    start_node = input("Enter the starting node for BFS: ")
    visited_nodes = bfs(graph, [start_node], [])

    print("Breadth-First Search:")
    print(visited_nodes)

if __name__ == "__main__":
    main()
"""OUTPUT
Enter the number of edges in the graph: 6
Enter the graph edges (node1 node2) one per line:
0 1
0 2
1 2
1 3
2 4
3 4
Enter the starting node for BFS: 0
Breadth-First Search:
['0', '1', '2', '3', '4']
=== Code Execution Successful ==="""
