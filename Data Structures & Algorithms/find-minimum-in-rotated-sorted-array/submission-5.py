# ceiling: O(n^3)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] > nums[r]:
                l += 1
                continue
            else:
                return nums[l]

        return nums[r]
        
        
# Time: O(n)
# Space: O(n)

# [1,2,3,4,5,6]

# Rotate 4 times        
# [6,1,2,3,4,5]
# [5,6,1,2,3,4]
# [4,5,6,1,2,3]
# [3,4,5,6,1,2]

#  l         r
# [3,4,5,6,1,2]
# l > r
# move left

#    l       r
# [3,4,5,6,1,2]
# l > r
# move left

#      l     r
# [3,4,5,6,1,2]
# l > r
# move left

#        l   r
# [3,4,5,6,1,2]
# l > r
# move left


#          l r
# [3,4,5,6,1,2]
# l < r
# res = l
