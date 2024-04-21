class Stack:
    def __init__(self, maxsize):
        self.storage = [None] * maxsize
        self.maxsize = maxsize
        self.length = -1

    def isempty(self):
        if self.length == -1:
            return True
        else:
            return False

    def isfull(self):
        if self.length == self.maxsize-1:
            return True
        else:
            return False

    def push(self, value):
        if self.isfull():
            raise Exception('Stack is full')
        else:
            self.length += 1
            self.storage[self.length] = value
            return True

    def pop(self):
        if self.isempty():
            raise Exception('Stack is empty')
        else:
            val = self.storage[self.length]
            self.storage[self.length] = None
            self.length -= 1
            return val

    def __str__(self):
        return '->'.join([str(x) for x in self.storage])


if __name__ == '__main__':
    s = Stack(3)
    print(s, s.isfull(), s.isempty(), s.length)
    s.push(2)
    s.push(1)
    s.push(3)
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s, s.isfull(), s.isempty(), s.length)
