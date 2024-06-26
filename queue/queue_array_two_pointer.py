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
            raise Exception('Queue is empty')
        else:
            return self.storage[self.front + 1]

    def enqueue(self, value):
        if not self.is_full():
            self.rear += 1
            self.storage[self.rear] = value
        else:
            raise Exception('Queue is full')

    def dequeue(self):
        if not self.is_empty():
            self.front = self.front + 1
            temp = self.storage[self.front ]
            self.storage[self.front] = None
# Resetting front rear to -1 to utilize unused space. if both are same i.e queue is empty
            if self.rear == self.front:
                self.rear = -1
                self.front = -1
            return temp
        else:
            self.front = -1
            self.rear = -1
            raise Exception('Queue is empty')

    def __str__(self):
        return ''.join(str(self.storage))


if __name__ == '__main__':
    try:
        q = Queue(2)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
    except Exception as e:
        print(e)
    try:
        q = Queue(2)
        q.enqueue(2)
        q.dequeue()
        q.dequeue()
    except Exception as e:
        print(e)


