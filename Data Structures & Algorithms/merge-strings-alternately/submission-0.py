class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        i, j = 0, 0
        output = ""
        while i < w1 and j < w2:
            output += word1[i]
            output += word2[j]
            i += 1
            j += 1
        
        if i < w1:
            output += word1[i:]
        if j < w2:
            output += word2[j:]
        return output
        