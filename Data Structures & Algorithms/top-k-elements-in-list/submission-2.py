import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        heap = []
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        for key, val in hashmap.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        print(heap)
        return [key for _ , key in heap]

        
        



        