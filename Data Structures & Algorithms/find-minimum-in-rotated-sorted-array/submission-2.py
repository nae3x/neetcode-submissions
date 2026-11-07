# ceiling: O(n^3)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min:
                min = nums[i]

        return min
        
# Time: O(n)
# Space: O(n)

# [1,2,3,4,5,6]

# Rotate 4 times        
# [6,1,2,3,4,5]
# [5,6,1,2,3,4]
# [4,5,6,1,2,3]
# [3,4,5,6,1,2]
