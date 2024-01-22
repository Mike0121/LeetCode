class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        all_subsets = []
        subset = []

        def generate_subsets(i, subset):
            all_subsets.append(subset)
            
            if i == len(nums):
                return None

            for j in range(i, len(nums)):
                generate_subsets(j + 1, subset + [nums[j]])

        generate_subsets(0, [])

        return all_subsets