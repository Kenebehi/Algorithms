def count_connected_components(edges):
    """
    Count num of connectec components
    :param graph:
    :return:
    """
    count = 0
    visited = set()
    graph = build_graph(edges)

    for node in [*graph]:
        if node not in visited:
            if _traverse_graph(edges, node, visited):
                count += 1
        print(f"node is {node}  in visited = {visited}")
    return count


def _traverse_graph(edges, node, visited):
    graph = build_graph(edges)
    stack = [node]
    while len(stack) > 0:
        current = stack.pop()
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    return True


def build_graph(edges):
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
print(count_connected_components(edges))
print(build_graph(edges))