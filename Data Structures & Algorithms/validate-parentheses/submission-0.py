class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {'}' : "{", "]" : "[", ")" : "("}
        for char in s:
            if char in mapp:
                if stack and mapp[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        