class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        countHashMap = defaultdict(int)
        countHashMap[0] = 1
        ans = 0
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            diff = cur_sum - k

            if diff in countHashMap:
                ans += countHashMap[diff]

            countHashMap[cur_sum] += 1


        return ans
