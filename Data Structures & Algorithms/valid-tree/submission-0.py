class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        from collections import defaultdict

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if not dfs(nei, node):
                        return False
                    elif not dfs(nei, parent):
                        return False
                    dfs(nei, node)
            return True
        
        return dfs(0, -1) and len(visited) == n
        