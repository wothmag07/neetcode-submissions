"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNewCopy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToNewCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldToNewCopy[curr]
            copy.next = oldToNewCopy[curr.next]
            copy.random = oldToNewCopy[curr.random]
            curr = curr.next
        return oldToNewCopy[head]

        