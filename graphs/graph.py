class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest):
        if self.adj_list.get(src, None):
            self.adj_list[src].append(dest)
        else:
            self.adj_list[src] = [dest]

        if self.adj_list.get(dest, None):
            self.adj_list[dest].append(src)
        else:
            self.adj_list[dest] = [src]

    def add_directed_weighted_edge(self, src, dest, weight):

        if self.adj_list.get(dest, None) is None:
            self.adj_list[dest] = []

        if self.adj_list.get(src, None):
            self.adj_list[src].append([dest, weight])
        else:
            self.adj_list[src] = [[dest, weight]]

    def __str__(self):
        return '\n'.join([str(k) + '= ' + str(v) for k, v in self.adj_list.items()])


if __name__ == '__main__':
    edges = [
        [0, 1], [1, 2], [0, 3], [3, 4],
        [4, 7], [3, 7], [6, 7], [4, 5],
        [4, 6], [5, 6]]
    g = Graph()
    for k, v in edges:
        g.add_edge(k, v)
    print(g)
    g1 = Graph()
    edges = [
        ['A', 'B', 6], ['A', 'D', 9], ['A', 'C', 10],
        ['B', 'D', 5], ['B', 'E', 16], ['B', 'F', 13],
        ['D', 'F', 8], ['D', 'H', 7],
        ['C', 'H', 5], ['C', 'D', 6], ['C', 'G', 21],
        ['E', 'G', 10],
        ['F', 'E', 4], ['F', 'G', 12], ['H', 'G', 14], ['H', 'F', 2]]
    for k, v, w in edges:
        g1.add_directed_weighted_edge(k, v, w)
    print(g1)
