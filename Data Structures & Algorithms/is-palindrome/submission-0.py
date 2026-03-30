class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = ''
        for char in s:
            if char.isalnum():
                out += char.lower()
        return out == out[::-1]


        