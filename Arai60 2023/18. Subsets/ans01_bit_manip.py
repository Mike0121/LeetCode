class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #brute-forth (ビット演算)
       
        N = len(nums)
        result = []

        for i in range(2 ** N):
        #for i in range(1 << N):
            subset = []
            for j in range(N):
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)

        return result