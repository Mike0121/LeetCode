class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []
        stack = []

        def generate_parenthesis_recursive(openN, endN):
            #ベースケース
            if openN == n and endN == n:
                answer.append(("").join(stack))
                return None

            if openN < n:
                stack.append("(")
                generate_parenthesis_recursive(openN+1, endN)
                stack.pop()

            if endN < openN:
                stack.append(")")
                generate_parenthesis_recursive(openN, endN+1)
                stack.pop()
            
        generate_parenthesis_recursive(0, 0)

        return answer