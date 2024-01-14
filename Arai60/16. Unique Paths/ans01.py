class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #並び替え(数学)による解答
        import math
        if m > n:
            return math.comb(m-1 + n-1, n-1)
        else:
            return math.comb(m-1 + n-1, m-1)