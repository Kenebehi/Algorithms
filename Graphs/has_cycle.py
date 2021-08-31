def has_cycle(graph, src):
    """

    :param graph:
    :return:
    """
    queue = ["f"]

    while len(queue) > 0:
        curr = queue.pop(0)
        print(f"this ths the queue {queue} and the current value {curr} and source {src}")
        # then there is a loop
        if curr == src:
            return True
        for n in graph[curr]:
            queue.append(n)
    return False


graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "k": ["h"],
    "h": [],
    "i": []

}
print(has_cycle(graph, "k"))
