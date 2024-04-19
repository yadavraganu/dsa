def depth_first_traversal_iterative(graph, node):
    stack = []
    visited = set()
    stack.append(node)

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
        print(f'Visited Node {current_node}')

        for neighbour in graph[current_node][::-1]:
            if neighbour not in visited:
                stack.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2, 3], 1: [4, 5], 2: [6], 3: [7], 4: [1], 5: [1], 6: [2], 7: [3]}
    depth_first_traversal_iterative(graph, 0)
