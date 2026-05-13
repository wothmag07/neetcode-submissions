class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        def partition(nums, lptr, rptr):
            mid = (lptr + rptr) // 2
            nums[mid], nums[lptr+1] = nums[lptr+1], nums[mid]

            if nums[lptr] > nums[rptr]:
                nums[lptr], nums[rptr] = nums[rptr], nums[lptr]
            
            if nums[lptr+1] >  nums[rptr]:
                nums[lptr+1], nums[rptr] = nums[rptr], nums[lptr+1]
            
            if nums[lptr] > nums[lptr+1]:
                nums[lptr], nums[lptr+1] = nums[lptr+1], nums[lptr]
            

            pivot = nums[lptr+1]
            i = lptr + 1
            j = rptr

            while True:
                while True:
                    i += 1
                    if not nums[i] < pivot:
                        break
                while True:
                    j -= 1
                    if not nums[j] > pivot:
                        break
                
                if i > j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            
            nums[lptr+1], nums[j] = nums[j], nums[lptr+1]

            return j
        
        def quicksort(nums, lptr, rptr):
            if rptr <= lptr+1:
                if rptr == lptr+1 and nums[rptr] < nums[lptr]:
                    nums[lptr], nums[rptr] = nums[rptr], nums[lptr]
                return
            
            j = partition(nums, lptr, rptr)
            quicksort(nums, lptr, j-1)
            quicksort(nums, j+1, rptr)
        
        quicksort(nums, 0, len(nums)-1)
        return nums

