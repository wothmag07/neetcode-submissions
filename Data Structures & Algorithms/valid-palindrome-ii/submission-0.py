class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        def isPalindrome(s, lptr, rptr):
            while lptr < rptr:
                if s[lptr] != s[rptr]:
                    return False
                lptr += 1
                rptr -= 1
            return True
        
        lptr, rptr = 0, len(s)-1
        while lptr < rptr:
            if s[lptr] != s[rptr]:
                return isPalindrome(s, lptr+1, rptr) or isPalindrome(s, lptr, rptr-1)
            lptr += 1
            rptr -= 1
        return True

        