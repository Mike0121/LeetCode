class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1

        #無限ループのテストとして適切なのは下記のパターン
        #1.targetあり、l=r
        #2.targetなし、l=r

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            #Case: Left side is sorted
            if nums[mid] >= nums[l]:
                #1-1.
                #Target is in the left side or not
                #targetがmidより大きい、もしくは、targetがlより小さい。
                #⇔targetは右側にある。
                if target > nums[mid] or target < nums[l]:
                    l =mid+1
                #1-2.
                else:
                    r = mid-1

            #Case: Right side is sorted
            else:
                #2-1.
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                #2-2.
                else:
                    l = mid+1

        return -1