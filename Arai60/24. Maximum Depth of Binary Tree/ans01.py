# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        def dfs(root, depth):
            if root == None:
                return depth

            left_depth = dfs(root.left, depth+1)
            right_depth = dfs(root.right, depth+1)

            return max(left_depth, right_depth)

        return dfs(root, 0)
            