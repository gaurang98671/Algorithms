class Node:
    def __init__(self, val):
        self.val = val
        self.isWord = False
        self.children = [None for x in range(26)]


class WordDictionary:

    def __init__(self):
        self.root = Node("*")

    def sol(self, node, word, curr, curr_path, ans, n=0):

        if curr == len(word) and node.isWord:
            ans.append(curr_path)

        if len(word) > curr and word[curr] == '.':

            for i in node.children:

                if i != None:
                    new_path = curr_path.copy()
                    new_path.append(i.val)
                    self.sol(i, word, curr + 1, new_path, ans, 1)

        elif len(word) > curr and node.children[ord(word[curr]) - ord('a')] != None:

            node = node.children[ord(word[curr]) - ord('a')]

            new_path = curr_path.copy()
            new_path.append(node.val)
            self.sol(node, word, curr + 1, new_path, ans, 1)

        if n == 0 or len(ans) > 0:
            return ans

    def addWord(self, word: str) -> None:

        node = self.root
        for i in word:
            if node.children[ord(i) - ord('a')] == None:
                new_node = Node(i)
                node.children[ord(i) - ord('a')] = new_node
                node = new_node
            else:
                node = node.children[ord(i) - ord('a')]
        node.isWord = True

    def search(self, word: str) -> bool:
        ans = self.sol(self.root, word, 0, [], [])
        return len(ans) > 0

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)