class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        ans = []

        #重複をなくすために、いったんnums1をdictに入れる。
        #O(n)
        for n in nums1:
            d[n] = 1

        #print(d)

        #nums2がdのkeyとして存在するかを確認。
        #double-checkを避けるため、dictを利用する。
        #O(m)
        for m in nums2:
            
            #mがdの中にあり、d[m]が0でない(まだ未登録)場合
            #O(1)
            if m in d and d[m]:
                #O(1)
                ans.append(m)
                d[m] -= 1

        #O(n + m)
        return ans
                
                






            