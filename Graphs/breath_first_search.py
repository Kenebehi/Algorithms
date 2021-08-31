def breath_first_search_iteration(graph, source="a"):
    """
    :param graph:
    :param source:
    :return:
    """
    queue = [source]
    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr)
        for n in graph[curr]:
            queue.append(n)


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
breath_first_search_iteration(graph)

