class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, maxsize):
        self.head = None
        self.tail = None
        self.length = 0
        self.maxsize = maxsize

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next


class Queue:
    def __init__(self, maxsize):
        self.linked_list = LinkedList(maxsize)

    def isfull(self):
        if self.linked_list.length == self.linked_list.maxsize:
            return True
        else:
            return False

    def isempty(self):
        if self.linked_list.length == 0:
            return True
        else:
            return False

    def enqueue(self, value):
        if not self.isfull():
            new_node = Node(value)
            if self.linked_list.head is None:
                self.linked_list.head = new_node
                self.linked_list.tail = new_node
                self.linked_list.length += 1
            else:
                self.linked_list.tail.next = new_node
                self.linked_list.tail = new_node
                self.linked_list.length += 1
        else:
            raise Exception('Queue is full')

    def dequeue(self):
        if not self.isempty():
            if self.linked_list.head == self.linked_list.tail:
                deleted_node = self.linked_list.head
                self.linked_list.head = None
                self.linked_list.tail = None
                self.linked_list.length = 0
                return deleted_node.value
            else:
                deleted_node = self.linked_list.head
                self.linked_list.head = self.linked_list.head.next
                self.linked_list.length -= 1
                return deleted_node.value
        else:
            raise Exception('Queue is empty')

    def __str__(self):
        return '->'.join([str(i) for i in self.linked_list])


if __name__ == '__main__':
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q, q.linked_list.length)
    print(q.dequeue())
    q.dequeue()
    print(q.dequeue())
    print(q, q.linked_list.length)
