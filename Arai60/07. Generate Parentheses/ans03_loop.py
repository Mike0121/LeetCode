class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #Try(loop)
        stack = [(0, 0, "")]
        answer = []

        while stack:
            open_count, end_count, s = stack.pop()

            if open_count == end_count == n:
                answer.append(s)
                continue

            if open_count < n:
                stack.append((open_count+1, end_count, s + "("))

            if end_count < open_count:
                stack.append((open_count, end_count+1, s + ")"))

        return answer