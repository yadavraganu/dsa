class Heap:
    def __init__(self, heap_typ):
        self.heap = []
        self.heap_size = 0
        self.heap_typ = heap_typ

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

    def extract_heapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        swap = index
        if self.heap_typ == 'max':
            if right <= self.heap_size - 1 and self.heap[right] > self.heap[index]:
                swap = right
                self.heap[right], self.heap[index] = self.heap[index], self.heap[right]
            elif left <= self.heap_size - 1 and self.heap[index] < self.heap[left]:
                self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
                swap = left
        elif self.heap_typ == 'min':
            if right <= self.heap_size - 1 and self.heap[right] < self.heap[index]:
                swap = right
                self.heap[right], self.heap[index] = self.heap[index], self.heap[right]
            elif left <= self.heap_size - 1 and self.heap[index] > self.heap[left]:
                self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
                swap = left
        if swap != index:
            self.extract_heapify(swap)

    def insert(self, value):
        self.heap.append(value)
        self.heapify(self.heap_size, self.heap_typ)
        self.heap_size += 1

    def extract(self):
        if self.heap_size < 1:
            print('Heap size is zero')
            return False
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped_node = self.heap.pop()
        self.heap_size -= 1
        self.extract_heapify(0)
        return popped_node


heap = Heap('min')
heap.insert(2)
heap.insert(50)
heap.insert(1)
heap.insert(3)
print(heap.heap)
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.heap)
