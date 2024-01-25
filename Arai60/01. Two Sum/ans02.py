class Solution(object):
    def twoSum(self, nums, target):
        hash_map = defaultdict()

        for index, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target-num], index]
            
            hash_map[num] = index

        return None
