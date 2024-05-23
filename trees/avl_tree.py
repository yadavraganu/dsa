class AvlNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


class AvlTree:
    def __init__(self, root):
        self.data = root
        self.left = None
        self.right = None
        self.height = 0

    def get_height(self, root):
        if root is None:
            return 0
        else:
            return root.height

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.left)

    def insert(self, root, data):
        if root is None:
            return
        if data <= root.data:
            if root.left is None:
                root.left = AvlNode(data)
            else:
                self.insert(root.left, data)
        if data > root.data:
            if root.right is None:
                root.right = AvlNode(data)
            else:
                self.insert(root.right, data)

        root.height = 1 + max(self.get_height(root.right), self.get_height(root.left))
        print(self.get_balance(root))


if __name__ == '__main__':
    avl = AvlTree(3)
    avl.insert(avl, 2)
    avl.insert(avl, 4)
    print(avl.get_height(avl))
