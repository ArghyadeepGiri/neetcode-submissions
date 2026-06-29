class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        if not nums:
            return res
        nums = sorted(nums)
        d = {}
        for num in nums:
            if num-1 in d:
                d[num] = d[num-1] + 1
            else:
                d[num] = 1

        return max([v for k, v in d.items()])

            

        