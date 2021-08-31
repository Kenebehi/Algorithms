def has_path(graph, src, target):
    """
    Time complexity: O(e) where e is numner of edges
    Space complexity: O(N) where n is number of nodes
    :param graph:
    :param src:
    :param target:
    :return:
    """
    stack = [src]

    while len(stack) > 0:
        curr = stack.pop()
        if curr == target:
            return True
        for n in graph[curr]:
            stack.append(n)
    return False


graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}
print(has_path(graph, src="f", target="k"))
