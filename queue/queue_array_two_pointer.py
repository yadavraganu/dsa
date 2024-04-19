class Queue:
    def __init__(self, size):
        self.size = size
        self.storage = [None] * self.size
        self.front = -1
        self.rear = -1

    def is_full(self):
        if self.rear == self.size - 1:
            return True
        else:
            return False

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def peek(self):
        if self.front == self.rear:
            print('Queue is empty')
            return False
        else:
            return self.storage[self.front + 1]

    def enqueue(self, value):
        if not self.is_full():
            self.rear += 1
            self.storage[self.rear] = value
        else:
            print('Queue is full')

    def dequeue(self):
        if not self.is_empty():
            temp = self.storage[self.front + 1]
            self.storage[self.front + 1] = None
            self.front += 1
# Resetting front rear to -1 to utilize unused space. if both are same i.e queue is empty
            if self.rear == self.front:
                self.rear = -1
                self.front = -1
            return temp
        else:
            self.front = -1
            self.rear = -1
            print('Queue is empty')

    def __str__(self):
        return ''.join(str(self.storage))


if __name__ == '__main__':
    q = Queue(2)
    q.enqueue(2)
    q.enqueue(3)
    print(q.front, q.rear)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    q.enqueue(5)
    print(q.front, q.rear)
    q.peek()
    print(q)
