class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False    


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end
            
            char = word[idx]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, idx+1):
                        return True
                return False
            
            if char not in node.children:
                return False
            
            return dfs(node.children[char], idx+1)
        
        return dfs(self.root, 0)
        
