class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()

        for n in s:
            #If "n" is for left-side brankets
            if n == "(" or n == "{" or n == "[":
                stack.append(n)
            else:
                #stack is empty
                if len(stack) == 0:
                    return False

                elif n == ")" and stack[-1] == "(":
                    stack.pop()

                elif n == "}" and stack[-1] == "{":
                    stack.pop()

                elif n == "]" and stack[-1] == "[":
                    stack.pop()

                else:
                    return False
        
        if len(stack) == 0:
            return True

