class Solution:
    def isPalindrome(self, s: str) -> bool:
        lptr, rptr = 0, len(s)-1
        while lptr < rptr:
            while lptr < rptr and not s[lptr].isalnum():
                lptr += 1
            while lptr < rptr and not s[rptr].isalnum():
                rptr -= 1
            if s[lptr].lower() != s[rptr].lower():
                return False
            lptr, rptr = lptr + 1, rptr - 1
        return True


        