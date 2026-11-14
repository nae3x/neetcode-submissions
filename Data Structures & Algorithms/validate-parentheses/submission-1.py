class Solution:
    def isValid(self, s: str) -> bool:
        pairMap = { 
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for i in range(len(s)):

            if pairMap.get(s[i]) is None:
                stack.append(s[i])
            else:
                try:
                    item = stack.pop()
                except:
                    item = None
                
                if pairMap.get(s[i]) != item:
                    return False

        return len(stack) == 0
        