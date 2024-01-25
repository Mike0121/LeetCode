class Solution:
    def isValid(self, s: str) -> bool:
        kakko_table = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for kakko in s:
            if kakko in kakko_table:
                stack.append(kakko)
                continue

            if len(stack) == 0:
                return False
            
            if kakko_table[stack[-1]] != kakko:
                return False

            stack.pop()

        return True if len(stack) == 0 else False