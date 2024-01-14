class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hash Map
        hash_map = {}

        for s in strs:
            sorted_s = ("").join(sorted(s))
            
            if sorted_s not in hash_map:
                hash_map[sorted_s] = [s]

            else:
                hash_map[sorted_s].append(s)

        return list(hash_map.values())