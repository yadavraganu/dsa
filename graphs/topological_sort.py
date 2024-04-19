def topological_sort_util(graph, node, stack,visited):
    stack.append(node)
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                stack.append(neighbour)
        topological_sort_util(graph, current_node,stack,visited)
        return current_node
def topological_sort(graph, node):
    stack = []
    visited = set()
    for i in graph:
        node = topological_sort_util(graph,node,stack,visited)
        print(node)

if __name__ == '__main__':
    graph = {0: [1, 2, 3], 1: [4, 5], 2: [6], 3: [7], 4: [1], 5: [1], 6: [2], 7: [3]}
    topological_sort(graph, 0)