# ceiling: 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()

        return nums[0]

# [1,2,3,4,5,6]

# Rotate 4 times        
# [6,1,2,3,4,5]
# [5,6,1,2,3,4]
# [4,5,6,1,2,3]
# [3,4,5,6,1,2]
