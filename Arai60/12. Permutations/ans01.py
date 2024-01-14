class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def back_tracking(i):

            if i == len(nums):
                ans.append(nums[:])

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                back_tracking(i+1)
                nums[i], nums[j] = nums[j], nums[i]
                
        back_tracking(0)

        return ans