class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        output = defaultdict(list)
        
        
        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord(char) - ord('a')] +=1
            key = tuple(freq)
            output[key].append(word)
        
        return list(output.values())

             
            
        