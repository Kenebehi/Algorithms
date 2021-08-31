def depth_first_search_iteration(graph, source="a"):
    """
    :param graph:
    :param source:
    :return:
    """
    stack = [source]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr)
        for n in graph[curr]:
            stack.append(n)


def depth_first_search_recursion(graph, source="a"):
    """

    :param graph:
    :param source:
    :return:
    """
    print(source)
    for n in graph[source]:
        depth_first_search_recursion(graph, n)


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
depth_first_search_iteration(graph)
print("==========================")
depth_first_search_recursion(graph)
