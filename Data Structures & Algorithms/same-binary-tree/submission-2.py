# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque([p])
        queue2 = deque([q])
        while queue1 and queue2:
            for _ in range(len(queue1)):
                nodep = queue1.popleft()
                nodeq = queue2.popleft()

                if nodep is None and nodeq is None:
                    continue
                
                if nodep is None or nodeq is None or nodep.val != nodeq.val:
                    return False
                
                queue1.append(nodep.left)
                queue1.append(nodep.right)
                queue2.append(nodeq.left)
                queue2.append(nodeq.right)
        
        return True