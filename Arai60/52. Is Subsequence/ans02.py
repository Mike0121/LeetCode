class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True

        s_index = 0

        for t_char in t:

            if s[s_index] != t_char:
                continue

            s_index += 1

            if s_index == len(s):
                return True

        return False