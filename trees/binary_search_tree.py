class BstNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def add_node(root_node, val):
    if root_node is None:
        return BstNode(val)
    if val <= root_node.val:
        if root_node.left is not None:
            add_node(root_node.left, val)
        else:
            root_node.left = BstNode(val)
    if val > root_node.val:
        if root_node.right is not None:
            add_node(root_node.right, val)
        else:
            root_node.right = BstNode(val)


def pre_order_traversal(root_node):
    if root_node is None:
        return
    print(root_node.val)
    pre_order_traversal(root_node.left)
    pre_order_traversal(root_node.right)


def post_order_traversal(root_node):
    if root_node is None:
        return
    pre_order_traversal(root_node.left)
    pre_order_traversal(root_node.right)
    print(root_node.val)


def in_order_traversal(root_node):
    if root_node is None:
        return
    pre_order_traversal(root_node.left)
    print(root_node.val)
    pre_order_traversal(root_node.right)


def delete_node(root_node, value):
    if root_node is None:
        return None
    if value > root_node.val:
        root_node.right = delete_node(root_node.right, value)
    elif value < root_node.val:
        root_node.left = delete_node(root_node.left, value)
    else:
        if root_node.left is None and root_node.right is not None:
            return root_node.right
        elif root_node.right is None and root_node.left is not None:
            return root_node.left
        elif root_node.right is None and root_node.left is None:
            return root_node
        else:
            temp = root_node.right
            while temp.left:
                temp = temp.left
                root_node.val = temp.val
                print(root_node.val, temp)
                root_node.right = delete_node(root_node.right, temp.val)


def delete_bst(root_node):
    root_node.val = None
    root_node.left = None
    root_node.right = None


if __name__ == '__main__':
    root = BstNode(1)
    add_node(root, 3)
    add_node(root, 4)
    pre_order_traversal(root)
    root = delete_node(root, 1)
    pre_order_traversal(root)
