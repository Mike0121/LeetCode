# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        #print(preorder, inorder)
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        #print(root.val, mid)

        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:len(preorder)], inorder[mid+1:len(inorder)])


        return root