class Queue:
    def __init__(self, size):
        self.size = size
        self.storage = [None] * self.size
        self.pointer = -1

    def is_full(self):
        if self.pointer == self.size - 1:
            return True
        else:
            return False

    def is_empty(self):
        if self.pointer == -1:
            return True
        else:
            return False

    def peek(self):
        if self.pointer == -1:
            print('Queue is empty')
            return False
        else:
            return self.storage[0]

    def enqueue(self, value):
        if not self.is_full():
            self.pointer += 1
            self.storage[self.pointer] = value
        else:
            print('Queue is full')

    def dequeue(self):
        temp = self.storage[0]
        if not self.is_empty():
            for i in range(0, self.size - 1):
                self.storage[i] = self.storage[i + 1]
            self.storage[self.pointer] = None
            self.pointer -= 1
            return temp
        else:
            print('Queue is empty')

    def __str__(self):
        return ''.join(str(self.storage))


if __name__ == '__main__':
    q = Queue(3)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.peek())
    print(q)
