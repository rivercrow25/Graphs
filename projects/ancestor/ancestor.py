
def earliest_ancestor(ancestors, starting_node):
    graph = find_child(ancestors)
    ancestor = attempt(graph, starting_node)
    return ancestor


def find_child(lst):
    graph = {}
    for pair in lst:
        if pair[1] in graph:
            graph[pair[1]].append(pair[0])
        else:
            graph[pair[1]] = [pair[0]]
    return graph


def attempt(graph, starting_node):
    stack = []
    stack.append([starting_node])
    visited = set()

    while len(stack) > 0:
        path = stack.pop()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v in graph:
                for parent in graph[v]:
                    c = list(path)
                    c.append(parent)
                    stack.append(c)

    if len(path) > 1:
        return path[-1]
    else:
        return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 11)
