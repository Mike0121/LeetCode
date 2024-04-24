class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #try
        current_sum = 0
        ans = nums[0]
        start = 0
        end = 0

        while end < len(nums):
            
            current_sum = max(nums[end], current_sum+nums[end])

            if current_sum > ans:
                ans = current_sum
            
            end += 1

        return ans