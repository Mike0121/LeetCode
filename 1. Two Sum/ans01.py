class Solution(object):
    def twoSum(self, nums, target):
        HashMap = defaultdict()

        for i, n in enumerate(nums):

            if n in HashMap:
                return [HashMap[n], i]

            HashMap[target - n] = i

        else:
            return None
