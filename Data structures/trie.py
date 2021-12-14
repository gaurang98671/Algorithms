class Node:
    def __init__(self, val):
        self.val = val
        self.children = [ None for x in range(26)]
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node("*")

    def insertNode(self, key):
        node = self.root
        for i in key:
            if node.children[ord(i) - ord('a')] is None:
                new_node = Node(i)

                node.children[ord(i) - ord('a')] = new_node
                node = new_node
            else:
                node = node.children[ord(i) - ord('a')]

        node.isWord = True

    def contains(self, key):
        node = self.root
        for i in key:

            if node.children[ord(i) - ord('a')] is None:
                return False
            else:
                node = node.children[ord(i) - ord('a')]
        return node.isWord

if __name__ == '__main__':
    trie = Trie()

    trie.insertNode("hello")
    print(trie.contains("hello"))
    trie.insertNode("helloo")
    print(trie.contains("helloo"))


