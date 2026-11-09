# Ceiling: O(n ^ 2) becuase s.length is 0 - 50,000, so half of 10^5. Therefore approximately should aim for n ^ 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        highestSubstring = 0
        
        
        for char in s:
            if char in window:
                posChar = window.index(char)
                window = window[posChar + 1:]
                window.append(char)
                # print(char,posChar, window)
                continue

            window.append(char)
            highestSubstring = max(highestSubstring, len(window))
            # print(char, window)
            
        return highestSubstring

# Time: O(n^2) because we have nested loop and window could be equal to s if every chars are unique
# Space: O(n) becuase window grow acording to s

# s="anviaj"
# anviaj
# a = 1
# an = 2
# anv = 3
# anvi = 4
# anvia X => Cut a = nvia = 4
# nviaj = 5
# break => res = 5

# anvia X => Cut a and its backward = nvia = 4
# anviv X => Cut v and its backward = iv = 4