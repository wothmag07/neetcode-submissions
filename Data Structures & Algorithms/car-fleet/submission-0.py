class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        """
        target=10
        position=[4,1,0,7]
        speed=[2,2,1,1]

        pairs = [(7,1),(4,2),(1,2),(0,1)]
        stack = [10]
        """

        stack = []
        for p, s in pairs:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)