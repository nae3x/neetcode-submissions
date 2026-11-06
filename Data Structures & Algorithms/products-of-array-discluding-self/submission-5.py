class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefix_storage = []
        for i in range(len(nums)):
            latest_value = prefix * nums[i]
            prefix_storage.append(latest_value)
            prefix = latest_value

        suffix = 1
        suffix_storage = [1] * len(nums) # For insert from back to front
        for i in range(len(nums) - 1, -1, -1):
            latest_value = suffix * nums[i]
            suffix_storage[i] = latest_value
            suffix = latest_value

        res = []
        for i in range(len(nums)):
            if i - 1 == -1:
                res.append(1 * suffix_storage[i + 1])
            elif i + 1 >= len(suffix_storage):
                res.append(prefix_storage[i - 1] * 1)
            else:
                res.append(prefix_storage[i - 1] * suffix_storage[i + 1])


        return res

# Time: O(n) + O(n) + O(n) = O(n) because we have sequencial loop on nums
# Space: O(n) + O(n) + O(n) = O(n) becuase prefix_storage, suffix_storage, and res grow according to nums
