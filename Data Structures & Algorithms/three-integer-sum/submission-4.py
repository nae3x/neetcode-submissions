# Ceiling: o(n ^ 3) because nums is between 3 to 3,000

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sort the input
        # Loop though the input (i)
            # Handle case:
                # i > 0 => Break
                # for i > 0 sum[i] = sum[i - 1] => continue
            # Use binary search to find a pair for i
                # target = the opposite of i = - i, so we get 0 from the triplet
                # < target => move to the right
                # > target => move to the left
                # = target => append to res
                    # Handle sum[l] == sum[l - 1] for until l < r => Dedup

        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = -nums[i]
                guess = nums[l] + nums[r]

                if guess < target:
                    l += 1
                elif guess > target:
                    r -= 1
                else:
                    threesum = [nums[i], nums[l], nums[r]]
                    res.append(threesum)
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
                    

# Time:
# Space: