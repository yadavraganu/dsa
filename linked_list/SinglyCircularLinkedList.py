class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyCircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            self.length += 1
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
            self.length += 1

    def __str__(self):
        current = self.head
        result = ''
        while current:
            result += str(current.value)
            if current.next == self.head:
                break
            current = current.next
            result += '->'
        return result

    def insert(self, index, value):
        assert (index in [0, -1]) or (0 <= index <= self.length - 1), 'Invalid Index'
        if index == 0:
            self.append(value)
        elif index == -1:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node


scll = SinglyCircularLinkedList()
scll.append(1)
scll.append(3)
print(scll, scll.length)
scll.insert(-1, 233)
print(scll, scll.length)
