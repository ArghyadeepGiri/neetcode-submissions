class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = l + 1
        maxLength = 1
        while r <= len(s):
            temp = set(s[l:r])
            
            length = len(temp)
            maxLength = max(length, maxLength)
            r = r + 1
            
            if r <= len(s) and s[r-1] in temp:
                l += 1
                r = l + 1
            
        return maxLength
