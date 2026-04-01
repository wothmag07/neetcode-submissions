class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        longest = 0
        lptr = 0
        for rptr in range(len(s)):
            while s[rptr] in charset:
                charset.remove(s[lptr])
                lptr += 1
            charset.add(s[rptr])
            longest = max(longest, rptr-lptr+1)
        return longest