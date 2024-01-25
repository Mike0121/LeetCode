class Solution(object):
    def twoSum(self, nums, target):
        number_to_index_table = defaultdict()

        for index, num in enumerate(nums):
            if target - num in number_to_index_table:
                return [number_to_index_table[target-num], index]
            
            number_to_index_table[num] = index

        return None
