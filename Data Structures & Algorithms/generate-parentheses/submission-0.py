class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def valid(s):
            open = 0
            for char in s:
                open += 1 if char=='(' else -1
                if open < 0:
                    return False
            return not open
        
        def dfs(s):
            if n * 2 == len(s):
                if valid(s):
                    output.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs("")
        return output


        