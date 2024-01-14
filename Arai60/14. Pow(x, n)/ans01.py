class Solution:
    #https://leetcode.com/problems/powx-n/solutions/3807610/python-simple-recursive/?envType=list&envId=rbx9vwti
    #Time:O(logN),Space:O(logN)
    @cache
    def myPow(self, x: float, n: int) -> float:
        
        #例外ケース
        if n == 0:
          return 1
        
        elif n == 1:
          return x

        elif n == -1:
          return 1/x

        half = self.myPow(x, n // 2)
        return half * half * self.myPow(x, n % 2)