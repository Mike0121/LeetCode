class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []

        def generate_parenthesis_recursive(s, left_num, right_num):

            if left_num == n and right_num == n:
                answer.append(s)
                return None

            if left_num < n:
                generate_parenthesis_recursive(s + "(", left_num+1, right_num)

            if right_num < left_num:
                generate_parenthesis_recursive(s + ")", left_num, right_num+1)


        generate_parenthesis_recursive("", 0, 0)
        return answer
