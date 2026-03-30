class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = [0]*26
        for char in s1:
            s1_freq[ord(char)-ord('a')] += 1
        word_freq = [0]*26
        for i in range(len(s1)):
            word_freq[ord(s2[i])-ord('a')] += 1
        
        if s1_freq == word_freq:
            return True
        
        for i in range(len(s1), len(s2)):
            word_freq[ord(s2[i]) - ord('a')] += 1
            word_freq[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_freq == word_freq:
                return True
        return False