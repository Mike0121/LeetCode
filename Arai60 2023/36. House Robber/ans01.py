class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i](i番目)の家にたどり着くまでの金額の最大値
        #⇔現在のi番目の家を盗むor盗まないの2択
        #⇔i番目の金額+dp[i-2] vs dp[i-1]
        #Create a dp table
        dp = [0] * len(nums)
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)

        dp[0], dp[1]        = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]