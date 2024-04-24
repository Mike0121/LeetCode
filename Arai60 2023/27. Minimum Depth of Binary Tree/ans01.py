# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        #左右のいずれのノードも存在しなかった場合
        #⇔leafノードの場合
        if root.left == None and root.right == None:
            return 1

        #左に進む場合(ただし、左が存在しなければ∞とする。)
        if root.left == None:
            left = float('inf')
        else:
            left = self.minDepth(root.left)

        #右に進む場合(ただし、右が存在しなければ∞とする。)
        if root.right == None:
            right = float('inf')
        else:
            right = self.minDepth(root.right)

        return min(left, right) + 1
        