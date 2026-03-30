class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def containsAll(sub, t):
            freq_t = {}
            for char in t:
                freq_t[char] = freq_t.get(char, 0) + 1
            for char in sub:
                if char in freq_t:
                    freq_t[char] -= 1
            return all(count <= 0 for count in freq_t.values())

        minLen = float('inf')
        result = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if containsAll(substring, t):
                    if len(substring) < minLen:
                        minLen = len(substring)
                        result = substring
        return result
            
        



        