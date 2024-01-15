1:✖(DP)、✖(再帰) 21.Oct.2023

1. maxにおいて、dp[i]が採用されるケース
nums = [1, 2, 3, 8, 7, 6]を考えればよい。

2. Quiz 下記を実行するとどうなる？
```
 class Solution:
     def lengthOfLIS(self, nums: List[int]) -> int:
         #再帰
         ans = 0
         memo = {}
        
         def dfs(i, prev_number):
             if nums[i] <= prev_number:
                 return 0
 
             if i in memo:
                 return memo[n]
             
             for j in range(i+1, n):
                 tmp_len = 1
                 tmp_len += dfs(j, nums[i])
             
             #再帰を抜けた段階でメモに記録
             memo[i] = tmp_len
 
             return memo[i]
 
         #for文を回し、すべてのiを先頭とした場合を試す。
         for n in range(len(nums)):
             tmp_ans = dfs(n, -float('inf'))
             ans = max(ans, tmp_ans)
 
         return ans
 ```


