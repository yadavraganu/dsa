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
