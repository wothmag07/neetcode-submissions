class FreqStack:

    def __init__(self):
        self.freq = {}
        self.maxcount = 0
        self.stacks = {}
        

    def push(self, val: int) -> None:
        valCount = self.freq.get(val, 0) + 1
        self.freq[val] = valCount
        if valCount > self.maxcount:
            self.maxcount = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)
        
        

    def pop(self) -> int:
        val = self.stacks[self.maxcount].pop()
        self.freq[val] -= 1
        if not self.stacks[self.maxcount]:
            self.maxcount -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()