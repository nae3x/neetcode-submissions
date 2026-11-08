class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return res

        while l <= r:
            middle = math.floor((l + r) / 2)
            guess = nums[middle]
            res = min(res, guess)

            if guess <= nums[r]:
                r = middle - 1
            else:
                l = middle + 1

        return res
