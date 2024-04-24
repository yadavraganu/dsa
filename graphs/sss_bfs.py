from graph import Graph


def sss_bfs(graph, node):
    visited = set()
    queue = [node]
    distance = {node: 0}
    path_traversal = {node: str(node)}
    while queue:
        popped_node = queue.pop(0)
        visited.add(popped_node)
        for neighbour in graph[popped_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path_traversal[neighbour] = path_traversal[popped_node] + '->' + str(neighbour)
                distance[neighbour] = distance[popped_node] + 1
    return distance, path_traversal


if __name__ == '__main__':
    edges = [
        [0, 1], [1, 2], [0, 3], [3, 4],
        [4, 7], [3, 7], [6, 7], [4, 5],
        [4, 6], [5, 6]]
    g = Graph()
    for k, v in edges:
        g.add_edge(k, v)
    print(g.adj_list)
    distance, path_traversal = sss_bfs(g.adj_list, 0)
    print(distance)
    print(path_traversal)
