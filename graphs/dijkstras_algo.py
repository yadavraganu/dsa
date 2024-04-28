from graph import Graph
import heapq


def sss_dij(graph, node):
    heap = []
    visited = set()
    distance = {node: 0}
    for i in g.adj_list:
        if i != node:
            distance.update({i: float('inf')})
    heapq.heappush(heap, (distance[node], node))
    while heap:
        popped_node = heapq.heappop(heap)
        if popped_node[0] not in visited:
            visited.add(popped_node)
        for i in graph.adj_list[popped_node[1]]:
            if i[0] not in visited:
                if distance[i[0]] > popped_node[0] + i[1]:
                    distance[i[0]] = popped_node[0] + i[1]
                heapq.heappush(heap, (distance[i[0]], i[0]))
    print(popped_node, distance)


if __name__ == '__main__':
    g = Graph()
    edges = [
        ['A', 'B', 6], ['A', 'D', 9], ['A', 'C', 10],
        ['B', 'D', 5], ['B', 'E', 16], ['B', 'F', 13],
        ['D', 'F', 8], ['D', 'H', 7],
        ['C', 'H', 5], ['C', 'D', 6], ['C', 'G', 21],
        ['E', 'G', 10],
        ['F', 'E', 4], ['F', 'G', 12], ['H', 'G', 14], ['H', 'F', 2]]
    for k, v, w in edges:
        g.add_directed_weighted_edge(k, v, w)
    print(g)
    sss_dij(g, 'A')
