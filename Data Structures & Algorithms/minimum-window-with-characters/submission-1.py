class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #Sliding window algo
        if not s or not t:
            return ''
        
        freq_t, window = {}, {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        have, need = 0, len(freq_t)
        res, resLen = [-1, -1], float('inf')
        lptr = 0

        for rptr in range(len(s)):
            char = s[rptr]
            window[char] = window.get(char, 0) + 1

            if char in freq_t and window[char] == freq_t[char]:
                have += 1
            
            while have == need:
                if rptr - lptr + 1 < resLen:
                    resLen = rptr - lptr + 1
                    res = [lptr, rptr]
                
                window[s[lptr]] -= 1
                if s[lptr] in freq_t and window[s[lptr]] < freq_t[s[lptr]]:
                    have -= 1
                lptr += 1
        lptr, rptr = res
        return "" if resLen == float('inf') else s[lptr : rptr+1]