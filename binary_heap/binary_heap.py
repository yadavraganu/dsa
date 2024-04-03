class Heap:
    def __init__(self, heap_typ):
        self.heap = []
        self.heap_size = 0
        self.heap_typ = 'max'

    def heapify(self, index, heap_typ):
        if index <= 0:
            return
        parent_node_idx = int(index / 2)
        if heap_typ == 'min':
            if self.heap[index] < self.heap[parent_node_idx]:
                self.heap[index], self.heap[parent_node_idx] = self.heap[parent_node_idx], self.heap[index]
        elif heap_typ == 'max':
            if self.heap[index] > self.heap[parent_node_idx]:
                self.heap[index], self.heap[parent_node_idx] = self.heap[parent_node_idx], self.heap[index]
        self.heapify(parent_node_idx, heap_typ)

    def insert(self, value):
        self.heap.append(value)
        self.heapify(self.heap_size, self.heap_typ)
        self.heap_size += 1


heap = Heap('max')
print(heap.heap, heap.heap_size)
heap.insert(2, )
heap.insert(3)
heap.insert(0)
heap.insert(3)
heap.insert(-1)
heap.insert(100)
print(heap.heap, heap.heap_size)
