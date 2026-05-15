class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return
        
        comp = path.split("/")
        print(comp)
        stack = []
        for folder in comp:
            if folder == "" or folder == ".":
                continue
            elif folder == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(folder)
        return "/" + "/".join(stack)
            
        