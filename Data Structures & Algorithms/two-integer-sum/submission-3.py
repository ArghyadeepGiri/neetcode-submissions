class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_d = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_d:
                return sorted([i, nums_d[diff]])
            nums_d[n] = i
        return []
        

