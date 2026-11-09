# Ceiling: O(n ^ 2) becuase s.length is 0 - 50,000, so half of 10^5. Therefore approximately should aim for n ^ 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        highestSubstring = 0

        l = 0
        for r, char in enumerate(s):
            dupPos = window.get(char)
            # print(dupPos)
            if dupPos is not None:
                # Clear the table
                # From l to f

                while l <= dupPos:
                    del window[s[l]]
                    l += 1
 
                # print(char,posChar, window)

            window[char] = r
            highestSubstring = max(highestSubstring, r - l + 1)
            # print(char, window, l, r)
            
        return highestSubstring

# Time: O(n^2) because we have nested loop and window could be equal to s if every chars are unique
# Space: O(n) becuase window grow acording to s

s="abcabcbb"

# window = {wnfo} <=> l
# l         f   r
# thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert => s