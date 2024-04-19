class Queue:
    def __init__(self, size):
        self.size = size
        self.storage = [None] * self.size
        self.front = -1
        self.rear = -1

    def is_full(self):
        # Queue is full when front at -1 & rear at end of the queue
        if self.front == -1 and self.rear == self.size - 1:
            return True
        # Queue is full rear is equal to front & it could happen at queue empty as well so ignoring -1 index
        elif (self.rear == self.front) and self.rear != -1:
            return True
        else:
            return False

    def is_empty(self):
        # Considering queue empty only when front & rear are -1
        if self.front == self.rear == -1:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        else:
            return self.storage[self.front + 1]

    def enqueue(self, value):
        if self.is_empty():
            self.rear = self.rear + 1
            self.storage[self.rear] = value
        elif self.is_full():
            raise Exception('Queue is full')
        else:
            self.rear = ((self.rear + 1) % self.size)
            self.storage[self.rear] = value

    def dequeue(self):
        if not self.is_empty():
            self.front = ((self.front + 1) % self.size)
            temp = self.storage[self.front]
            self.storage[self.front] = None
            # Resetting front rear to -1 to utilize unused space. if both are same i.e queue is empty
            if self.rear == self.front:
                self.rear = -1
                self.front = -1
            return temp
        else:
            raise Exception('Queue is empty')

    def __str__(self):
        return ''.join(str(self.storage))


if __name__ == '__main__':
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q, q.front, q.rear)
    q.dequeue()
    q.dequeue()
    print(q, q.front, q.rear, q.is_full())
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q, q.front, q.rear, q.is_full())
