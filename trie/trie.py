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
    if index == len(word):
        if root.isFinal:
            root.isFinal = False
            if len(root.children) == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        char = word[index]
        if char not in root.children:
            return False
        else:
            current_node = root.children[char]
    tobedeleted = delete(current_node, word, index + 1)
    if tobedeleted:
        del root.children[char]
        if len(root.children) > 0 or root.isFinal:
            return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    t = Trie()
    print(insert(t.root, 'sit'))
    delete(t.root, 'sit', 0)
    print(search(t.root, 'sit'))
    print('-'*10)
    print(t.root.children.keys())
    print(t.root.children['s'].children.keys())
    print(t.root.children['s'].children['i'].children.keys())
    print(t.root.children['s'].children['i'].children['t'].isFinal)
