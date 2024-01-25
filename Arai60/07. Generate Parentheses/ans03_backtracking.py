class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        all_valid_parenthesis = []
        open_count = 0
        end_count = 0
        parethensis_list = []

        def generate_parethesis(open_count, end_count):

            if open_count == n and end_count == n:
                all_valid_parenthesis.append(("").join(parethensis_list))

            if open_count < n:
                parethensis_list.append("(")
                generate_parethesis(open_count + 1, end_count)
                parethensis_list.pop()

            if end_count < open_count:
                parethensis_list.append(")")
                generate_parethesis(open_count, end_count + 1)
                parethensis_list.pop()

                
        generate_parethesis(0, 0)

        return all_valid_parenthesis