class Solution:
    def climbStairs(self, n: int) -> int:
        s1 = 0
        s2 = 1
        for i in range(n):
            res = s1 + s2
            s1 = s2
            s2 = res
        return res

        