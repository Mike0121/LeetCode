# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l, r = 0, len(nums)-1
        mid = (l+r)//2

        #2分探索のループを抜けたら終了
        if l > r:
            return

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[l:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:r+1])

        return root
        