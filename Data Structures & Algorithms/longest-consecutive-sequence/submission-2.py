class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        #print(numset)
        res = 0
        for num in nums:
            #print(num)
            length = 1
            if num-1 not in numset or num==0:
                k = num + 1
                while k in numset:
                    #print("here")
                    length += 1
                    k += 1
                res = max(res, length)
        return res

            

        