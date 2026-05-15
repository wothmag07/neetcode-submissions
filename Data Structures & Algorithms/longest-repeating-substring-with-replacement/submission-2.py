class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        maxfreq = 0
        lptr = 0
        freq = {}
        maxlen = 0

        for rptr in range(len(s)):
            freq[s[rptr]] = freq.get(s[rptr], 0) + 1

            maxfreq = max(maxfreq, freq[s[rptr]])
            windowsize = rptr-lptr+1
            if windowsize - maxfreq > k:
                freq[s[lptr]] -= 1
                lptr += 1
            maxlen = max(maxlen, rptr-lptr+1)
        return maxlen

        