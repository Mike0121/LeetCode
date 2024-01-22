class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        stack = [([], 0)]

        while stack:
            current_subset, current_index = stack.pop()
            all_subsets.append(current_subset)

            for n in range(current_index, len(nums)):
                stack.append((current_subset + [nums[n]], (n + 1)))

        return all_subsets
