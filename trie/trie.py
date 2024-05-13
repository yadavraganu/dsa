class TrieNode:
    def __init__(self):
        self.children = {}
        self.isFinal = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


def insert(root, word):
    current_letter = root
    for letter in word:
        if current_letter.children.get(letter) is None:
            current_letter.children[letter] = TrieNode()
        current_letter = current_letter.children.get(letter)
    current_letter.isFinal = True
    return 'Word inserted successfully'


def search(root, word):
    current_letter = root
    for letter in word:
        if current_letter.children.get(letter) is None:
            return False
        current_letter = current_letter.children.get(letter)
    if current_letter.isFinal:
        return True
    else:
        return False


def delete(root, word, index):
    current_node = root
    flag = False
    current_letter = word[index]
    if len(word) - 1 != index:
        flag = delete(current_node.children.get(current_letter), word, index + 1)
    print(current_node.children,current_node.children.get(current_letter).children, current_node.isFinal,current_letter)
    if len(current_node.children.get(current_letter).children) == 0 and current_node.isFinal:
        current_node.children.pop(current_letter)
        print(current_node.children)
        return True


if __name__ == '__main__':
    t = Trie()
    print(insert(t.root, 'sit'))
    print(insert(t.root, 'abc'))
    print(insert(t.root, 'sitty'))
    print(delete(t.root, 'sitty', 0))

    print(search(t.root, 'sit'))
    print(search(t.root, 'abc'))
    print(t.root.children)
    print(t.root.children['s'])
    print(t.root.children['s'].children)
    print(t.root.children['s'].children['i'].children)
    print(t.root.children['s'].children['i'].children['t'].children)
    print(t.root.children['s'].children['i'].children['t'].children['t'].children)

