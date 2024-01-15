class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        coins.sort()
        if amount == 0:
            return amount

        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a >= c:
                    #dp[a]: amount aを満たすのに最小のコインの必要枚数
                    dp[a] = min(dp[a], dp[a-c] + 1)

                else:
                    break

        #print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1