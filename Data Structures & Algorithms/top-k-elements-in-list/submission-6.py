class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            cache[nums[i]] = cache.get(nums[i], 0) + 1

        freq_table = [[] for i in range(len(nums) + 1)]
        for num, occur in cache.items():
            freq_table[occur].append(num)

        res = []
        for i in range(len(freq_table) -1, -1, -1):
            for num in freq_table[i]:
                res.append(num)

                if len(res) == k:
                    return res