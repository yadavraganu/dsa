class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        assert (index in [0, -1]) or (
            index <= self.length - 1 and index > 0
        ), "Invalid Index"
        if index == 0:
            self.prepend(value)
        elif index == -1:
            self.append(value)
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node = Node(value)
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, value):
        current = self.head
        index = 0
        found = False
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        if found != True:
            return -1

    def pop_first(self):
        if self.length == 0:
            return False
        else:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
            self.length -= 1
            return True

    def pop(self):
        if self.length == 0:
            return False
        else:
            popped_node = self.tail
            current = self.head
            while current.next != popped_node:
                current = current.next
            self.tail = current
            current.next = None
            self.length -= 1
            return True

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        assert (index >= 0 and index <= self.length - 1) or (
            index == -1
        ), "Invalid Index"
        current = self.head
        if index == 0:
            return self.head.value
        elif index == -1:
            return self.tail.value
        for _ in range(index):
            current = current.next
        return current.value

    def set(self, index, value):
        assert (index >= 0 and index <= self.length - 1) or (
            index == -1
        ), "Invalid Index"
        current = self.head
        if index == 0:
            self.head.value = value
            return True
        elif index == -1:
            self.tail.value = value
            return True
        for _ in range(index):
            current = current.next
        current.value = value
        return True
