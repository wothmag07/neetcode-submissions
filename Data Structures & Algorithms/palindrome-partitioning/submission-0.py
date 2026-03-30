class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        res = []

        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start, path):
            if start >= len(s):
                res.append(path[:])
                return
            for j in range(start, len(s)):
                if isPalindrome(s, start, j):
                    path.append(s[start: j+1])
                    dfs(j+1, path)
                    path.pop()
        dfs(0, [])
        return res


        
        
        
