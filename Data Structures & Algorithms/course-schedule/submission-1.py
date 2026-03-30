class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque

        if not prerequisites:
            return True
        
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        visited = 0
        while queue:
            course = queue.popleft()
            visited += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return visited == numCourses
            

        