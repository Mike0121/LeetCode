class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        unique_char_set = set()

        for right, char in enumerate(s):
            while char in unique_char_set:
                unique_char_set.discard(s[left])
                left += 1

            unique_char_set.add(char)
            result = max(result, right-left+1)

        return result