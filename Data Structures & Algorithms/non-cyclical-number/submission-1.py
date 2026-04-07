class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            output = 0
            while n:
                digit = n%10
                output += digit**2
                n //= 10
            return output
        slow, fast = n, sumOfSquares(n)
        while fast != 1 and slow != fast:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        
        return fast == 1
            


        


        