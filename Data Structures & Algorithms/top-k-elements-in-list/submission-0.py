class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        sol = []
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        sorted_res = sorted(d.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            sol.append(sorted_res[i][0])

        return sol
        