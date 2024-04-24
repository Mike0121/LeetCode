class Solution:
    def rob(self, nums: List[int]) -> int:

        def houseRobber(nums):

            #dp[i]:i番目の家までにたどり着くまでの最大の金額
            dp = [0]*len(nums)

            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    
            for n in range(2, len(nums)):

                dp[n] = max(dp[n-2] + nums[n], dp[n-1])

            return max(dp)

        #例外処理は今回、外側に書く必要あり
        #max(n, None)とできないので。
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))