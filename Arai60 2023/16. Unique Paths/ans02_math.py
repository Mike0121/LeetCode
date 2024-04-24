class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # The one-line below also works.
        # return math.comb((m - 1) * (n - 1), (n - 1))

        def calculate_factorial(integer_number):
            
            if integer_number <= 1:
                return 1

            return calculate_factorial(integer_number - 1) * integer_number

        def calculate_combinations(total_numbers, selected_numbers):

            return calculate_factorial(total_numbers)  // (calculate_factorial(selected_numbers) * calculate_factorial(total_numbers - selected_numbers))

        return calculate_combinations((m - 1) + (n - 1), n - 1)
