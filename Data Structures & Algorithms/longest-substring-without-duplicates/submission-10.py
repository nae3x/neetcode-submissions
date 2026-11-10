class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = {}

        l = 0
        for r, char in enumerate(s):
            dupPos = window.get(char)

            if dupPos is not None:
                while l <= dupPos:
                    del window[s[l]]
                    l += 1

            window[char] = r
            res = max(res, r - l + 1)

        return res 