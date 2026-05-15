class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        counter_t = Counter(t)
        lptr = 0
        required = len(counter_t)
        found = 0
        word_count = {}
        minsize = float("inf")
        min_window = ""
        for rptr in range(len(s)):
            char = s[rptr]
            word_count[char] = word_count.get(char, 0) + 1
            if char in counter_t and word_count[char] == counter_t[char]:
                found += 1

            while lptr <= rptr and found == required:
                window_size = rptr - lptr + 1
                if window_size < minsize:
                    minsize = window_size
                    min_window = s[lptr: rptr+1]
                left_char = s[lptr]
                word_count[left_char] -= 1

                if left_char in counter_t and word_count[left_char] < counter_t[left_char]:
                    found -= 1

                lptr += 1
        return min_window        