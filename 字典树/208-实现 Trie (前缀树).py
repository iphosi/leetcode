from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict()
        self.isEnd = False

    def insert(self, word: str) -> None:
        curr_node = self

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Trie()
            curr_node = curr_node.children[char]

        curr_node.isEnd = True

    def find_last_node(self, text: str):
        curr_node = self

        for char in text:
            if char not in curr_node.children:
                return None
            curr_node = curr_node.children[char]

        return curr_node

    def search(self, word: str) -> bool:
        last_node = self.find_last_node(word)
        return last_node is not None and last_node.isEnd

    def startsWith(self, prefix: str) -> bool:
        last_node = self.find_last_node(prefix)
        return last_node is not None
