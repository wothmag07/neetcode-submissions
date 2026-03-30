class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lptr = 0
        seen = set()
        maxLen = 0
        for rptr in range(len(s)):
            while s[rptr] in seen:
                seen.remove(s[lptr])
                lptr += 1
            seen.add(s[rptr])
            maxLen = max(maxLen, rptr-lptr+1)
        return maxLen


            
                


        