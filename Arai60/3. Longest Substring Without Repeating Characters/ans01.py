class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        char_set = set()

        for r in range(len(s)):
            #次に追加する文字が、char_set(現在の見ているsubstring)に重複している場合、
            #重複している文字が消えるまでsubstringの左側を小さくし続ける。
            while s[r] in char_set:
                #char_set.remove(s[l])
                char_set.discard(s[l])
                l += 1
            char_set.add(s[r])

            ans = max(ans, r-l+1)
        return  ans