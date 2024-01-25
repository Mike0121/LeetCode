class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        if n == 0:
            return []

        stack = [(0, 0, "")]
        
        while stack:
            openN, endN, current = stack.pop()

            if openN == n and endN == n:
                answer.append(current)
                continue

            if openN < n:
                stack.append((openN + 1, endN, current + "("))

            if endN < openN:
                stack.append((openN, endN + 1, current + ")"))

        return answer