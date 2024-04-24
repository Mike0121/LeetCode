class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        mincoin_to_amount = [float('inf')] * (amount+1)
        mincoin_to_amount[0] = 0
        coins.sort()

        for a in range(1, amount+1):
            for c in coins:
                if a - c < 0:
                    break
    
                mincoin_to_amount[a] = min(mincoin_to_amount[a-c]+1, mincoin_to_amount[a])

        return -1 if mincoin_to_amount[-1] == float('inf') else mincoin_to_amount[-1]