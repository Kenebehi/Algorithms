def largest_component(edges):
    """
    Counts the size of larges componenent
    size is number of nodes in graph
    :param edges:
    :return:
    """

    size = 0
    visited = set()
    nodes = [*_build_graph(edges)]

    for node in nodes:
        if _explore(edges, node, visited):
            size =  len(visited)
        return size


def _explore(edges, node, visited):
    graph = _build_graph(edges)

    stack = [node]
    while len(stack) > 0:
        curr = stack.pop()
        visited.add(curr)
        print(visited)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)
    return True


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
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]
print(largest_component(edges))