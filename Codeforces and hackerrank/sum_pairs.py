class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.numValue = 0


class MapSum:

    def __init__(self):
        self.root = Node("*")

    def insert(self, key: str, val: int) -> None:

        node = self.root
        for i in key:

            if i not in node.children:
                new_node = Node(i)
                node.children[i] = new_node
                node = new_node
            else:
                node = node.children[i]

        node.numValue = val

    def sol(self, node, ans, n=0):

        ans[0] += node.numValue

        for i in node.children:
            self.sol(node.children[i], ans, 1)

        if n == 0:
            return ans

    def sum(self, prefix: str) -> int:

        node = self.root
        found = True  # if prefix does not exist in trie
        for i in prefix:
            # check if i exists
            if i not in node.children:
                found = False
                break
            node = node.children[i]
        if found:
            ans = self.sol(node, [0])
            return ans[0]
        return 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)