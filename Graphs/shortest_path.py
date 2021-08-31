def shortest_path(edges):
    visited = set("w")
    return _shortest_path(edges, visited, "w", "z")


def _shortest_path(edges,  visited, src ="", dst=""):
    """
    Traverse from w to z
    :param edges:
    :return:
    """
    count = 0
    graph = _build_graph(edges)
    queue = [[src, 0]]

    while len(queue) > 0:
        print(queue)
        current = queue.pop(0)
        visited.add(current[0])

        if current[0] == dst:
            return current[1]

        for neighbor in graph[current[0]]:
            if neighbor not in visited:
                queue.append([neighbor, current[1] + 1])
    return -1


def _build_graph(edges):
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph


edges = [
    ["w", "x"],
    ["w", "v"],
    ["v", "z"],
    ["x", "y"],
    ["y", "z"]
]
print(shortest_path(edges))
