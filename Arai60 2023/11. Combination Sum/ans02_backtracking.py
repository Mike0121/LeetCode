class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_sum_combination = []
        current_sum_combination = []

        def find_all_combination_sum(i, target):

            if i == len(candidates):
                if target == 0:
                    all_sum_combination.append(current_sum_combination[:])
                return None

            if target - candidates[i] >= 0:
                current_sum_combination.append(candidates[i])
                find_all_combination_sum(i, target - candidates[i])
                current_sum_combination.pop()

            find_all_combination_sum(i + 1, target)

        find_all_combination_sum(0, target)

        return all_sum_combination