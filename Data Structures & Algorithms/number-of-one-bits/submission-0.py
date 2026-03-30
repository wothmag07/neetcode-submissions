class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        n=00000000000000000000000000001011
        1 << 0
        """
        output = 0
        for i in range(32):
            if (1 << i) & n:
                output += 1
        return output
        