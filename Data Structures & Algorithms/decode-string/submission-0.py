class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        curr_str = ""
        curr_num = 0
        stack = []
        for tok in s:
            if tok.isdigit():
                curr_num = curr_num*10 + int(tok)
            elif tok == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif tok == "]":
                last_str, num = stack.pop()
                curr_str = last_str + num * curr_str
            else:
                curr_str += tok
        return curr_str


        