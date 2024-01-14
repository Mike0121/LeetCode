class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0


        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r]-prices[l])
            #売却日は購入日より後でなければいけないかつ、
            #右側により小さい値があった場合、それを購入日としたほうが利益を最大化できるのは明らか
            else:
                l=r

            r+=1

        return max_profit