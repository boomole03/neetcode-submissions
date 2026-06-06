class Node: 
    def __init__(self):
        self.dictionary = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.wd = Node()

    def addWord(self, word: str) -> None:
        curr = self.wd

        for w in word: 
            if w not in curr.dictionary:
                curr.dictionary[w] = Node()
            curr = curr.dictionary[w]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            for idx in range(i, len(word)):
                c = word[idx]
                if c == '.':
                    for child in node.dictionary.values():
                        if dfs(child, idx+1):
                            return True
                    return False
                else: 
                    if c not in node.dictionary:
                        return False
                    node = node.dictionary[c]
            return node.word

        return dfs(self.wd, 0)
        
