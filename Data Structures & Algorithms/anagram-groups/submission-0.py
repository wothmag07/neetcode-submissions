from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for word in strs:
            char_freq = [0]*26
            for char in word:
                char_freq[ord(char) - ord('a')] += 1
            key = tuple(char_freq)
            out[key].append(word)
        return list(out.values())


            
        