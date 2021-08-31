def undirected_graphs(edges):
    """
    Find if there is a path between two nodes in a connected graph
    :param edges:
    :return:
    """
    return _undirected_graphs(edges)


def _undirected_graphs(edges, src="i", dst="m"):
    graph = build_graph(edges)
    print(graph)
    visited = set()

    stack = [src]
    while len(stack) > 0:
        curr = stack.pop()
        visited.add(curr)
        print(curr, dst, stack,visited)

        if curr == dst:
            return True
        for neighbor in graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)


def build_graph(edges):
    """
    :param edges:
    :return: adjacency list
    """
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph


# Edge list represent connection btw 2 nodes for ex ["i", "j"], represent
# connection btw i and j
edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]
print(undirected_graphs(edges))