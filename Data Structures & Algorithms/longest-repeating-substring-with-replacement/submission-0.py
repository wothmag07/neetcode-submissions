class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lptr = 0
        maxfreq, maxlen = 0, 0
        freq = {}
        for rptr in range(len(s)):
            freq[s[rptr]] = freq.get(s[rptr], 0) + 1

            maxfreq = max(maxfreq, freq[s[rptr]])

            windowsize = rptr - lptr + 1

            if windowsize - maxfreq > k:
                freq[s[lptr]] -= 1
                lptr += 1


            maxlen = max(maxlen, rptr - lptr + 1)
        return maxlen



        
        