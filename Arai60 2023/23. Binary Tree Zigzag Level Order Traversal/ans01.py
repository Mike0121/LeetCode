# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        stack = deque()
        stack.append(root)
        ans = []
        count = 0

        while stack:
            sub = []
            for n in range(len(stack)):

                if count % 2 == 0:
                    v = stack.popleft()
                    
                    if v.left:
                        stack.append(v.left)

                    if v.right:
                        stack.append(v.right)

                else:
                    v = stack.pop()

                    if v.right:
                        stack.appendleft(v.right)
                    
                    if v.left:
                        stack.appendleft(v.left)


                sub.append(v.val)

            ans.append(sub)
            count += 1

        return ans


        