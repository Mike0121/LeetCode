# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()

        #例外処理
        if root != None:
            queue.append(root)
        else:
            return ans

        while len(queue) > 0:
            tmp_ans = []
            for _ in range(len(queue)):
                #今回、処理の途中でpopにどんどん値が追加されていくが、
                #for文の回数が処理開始時のlen(queue)回なので、子ノード2つのみになる。
                #その時、"追加した順に"(⇔左から順に)queueから値を取り出す必要があるので、
                #popleftを利用する。

                #q = queue.pop()
                q = queue.popleft()
                print(q.val)
                tmp_ans.append(q.val)
                #1つのノードに対して、右と左それぞれの子子ノードをqに追加。
                if q.left != None:
                    queue.append(q.left)

                if q.right != None:
                    queue.append(q.right)

            #for分を抜けた段階、すなはち一旦あるノードから見た子ノードが
            #処理終わった段階で、2つの子ノードをansに追加。
            ans.append(tmp_ans)

        return ans