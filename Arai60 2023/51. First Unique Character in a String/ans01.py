class Solution:
    def firstUniqChar(self, s: str) -> int:
        #Optimized Solution O(N)
        HashMap = defaultdict(int)

        for i in s:
            HashMap[i] += 1

        for i, char in enumerate(s):
            if HashMap[char] == 1:
                return i

        else:
            return -1 
       