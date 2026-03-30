# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        if not root:
            return maxdepth
        stack = [(root, 1)]
        while stack:
            node, curr_depth = stack.pop()
            maxdepth = max(maxdepth, curr_depth)
            if node.left:
                stack.append((node.left, curr_depth + 1))
            if node.right:
                stack.append((node.right, curr_depth + 1))
        return maxdepth
        