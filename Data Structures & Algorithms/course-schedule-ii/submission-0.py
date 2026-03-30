class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        output = []

        graph = defaultdict(list)
        indegree = [0]*numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])
        while queue:
            course = queue.popleft()
            output.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return output if len(output) == numCourses else []