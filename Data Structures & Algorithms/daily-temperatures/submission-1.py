class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        result = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, idx = stack.pop()
                result[idx] = i - idx
            stack.append((temp, i))
        return result

        