class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        stones = [2,3,6,2,4]

        stones = [-2, -3, -6, -2, -4]
        """
        stones = [-s for s in stones]

        heapq.heapify(stones) # [-6,-4,-3,-2,-2] [-3,-2,-2,-2] [-2,-2,-1] [-1]

        while len(stones) > 1:
            first = heapq.heappop(stones) #-6, -3
            second = heapq.heappop(stones) #-4, -2
            if second > first: #-4 > -6, -1 > -2
                heapq.heappush(stones, first - second) #-4+4 = -2 #-1
        stones.append(0)
        return abs(stones[0])
        