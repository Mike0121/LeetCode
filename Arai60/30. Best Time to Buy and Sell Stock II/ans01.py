class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        ans = 0
        prev = float('inf')
        for p in prices:
            
            if p > prev:
                ans += p - prev
                prev = p

            else:
                prev = min(prev, p)
            
        return ans
        