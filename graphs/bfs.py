def breadth_first_traversal_iterative(graph, node):
    queue = []
    visited = set()
    queue.append(node)

    while queue:
        current_node = queue.pop(0)
        visited.add(current_node)

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return visited


if __name__ == '__main__':
    graph = {0: [1, 2, 3], 1: [4, 5], 2: [6], 3: [7], 4: [1], 5: [1], 6: [2], 7: [3]}
    breadth_first_traversal_iterative(graph, 0)

