from graph import Graph
import heapq


def sss_dij(graph, node):
    heap = []  # Initialize heap to pop the node with min distance everytime
    visited = set()  # keep a track of which node are visited
    distance = {node: 0}  # Initialize a distance map with 0 distances for starting node
    path = {node: str(node)}  # Initialize a path map to keep the track of path to reach destination
    for i in g.adj_list:  # Load the distance map with inf distance for other nodes
        if i != node:
            distance.update({i: float('inf')})
    heapq.heappush(heap, (distance[node], node))  # Push the first node to heap
    while heap:
        popped_node = heapq.heappop(heap)  # Pop the first node from heap
        if popped_node[0] not in visited:
            visited.add(popped_node)
        for i in graph.adj_list[popped_node[1]]:  # Access child nodes of popped node to add in heap & update distance
            if i[0] not in visited:
                # Update the distance of node to previous node's distance + weight if destination node's distance is less
                if distance[i[0]] > popped_node[0] + i[1]:
                    path[i[0]] = path[str(popped_node[1])] + '->' + i[0]
                    distance[i[0]] = popped_node[0] + i[1]
                heapq.heappush(heap, (distance[i[0]], i[0])) # Push the child node to heap
    return distance, path


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
    distance, path = sss_dij(g, 'A')
    print(distance)
    print(path)
