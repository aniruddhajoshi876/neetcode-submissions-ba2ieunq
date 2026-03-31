class TrieNode:
    def __init__(self):
       self.children = {}
       self.endword= False 
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endword = True
    

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if len(word) == index:
                return node.endword
            elif word[index].isalpha() and word[index] in node.children:
                return dfs(index+1, node.children[word[index]])
            elif word[index].isalpha() and word[index] not in node.children:
                return False
            elif word[index] == '.':
                for ch in node.children.values():
                    child = dfs(index+1, ch)
                    if child:
                        return True
                return False
        return dfs(0, self.root)

