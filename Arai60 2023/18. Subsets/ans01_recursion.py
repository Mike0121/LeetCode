class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []   
        def back_tracking(i, path):
            res.append(path)

            for j in range(i, len(nums)):
                back_tracking(j+1, path+[nums[j]])


        back_tracking(0, [])

        return res