class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []

        paratheses = {"]" : "[", "}" : "{", ")" : "("}
        for char in s:
            if char in paratheses:
                if stack and stack[-1] == paratheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return False if stack else True