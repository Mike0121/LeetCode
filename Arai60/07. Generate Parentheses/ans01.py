class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        stack = deque()

        def back_tracking(openN, endN):
            
            #ベースケース
            if openN == n and endN == n:
                ans.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                back_tracking(openN+1, endN)
                stack.pop()

            if endN < openN:
                stack.append(")")
                back_tracking(openN, endN+1)
                stack.pop()

        back_tracking(0, 0)

        return ans