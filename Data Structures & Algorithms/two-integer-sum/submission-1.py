class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if target-num in nums_dict:
                if i != nums_dict[target-num]:
                    return sorted([i, nums_dict[target-num]])
        return -1
