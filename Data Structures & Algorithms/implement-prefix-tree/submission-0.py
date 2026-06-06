class Node: 
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for w in word:
            w_i = ord(w.lower()) - ord('a')
            if not curr.children[w_i]:
                curr.children[w_i] = Node()
            curr = curr.children[w_i]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            w_i = ord(w.lower()) - ord('a')
            if not curr.children[w_i]:
                return False
            curr = curr.children[w_i]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            w_i = ord(w.lower()) - ord('a')
            if not curr.children[w_i]:
                return False
            curr = curr.children[w_i]
        return True
        
        