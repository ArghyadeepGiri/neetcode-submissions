class Solution:
    def convert_to_dict(self, s):
        d = {}
        for ch in s:
            if ch in d:
                d[ch] +=1
            else:
                d[ch] =1
        return d
    def isAnagram(self, s: str, t: str) -> bool:
        ds = self.convert_to_dict(s)
        dt = self.convert_to_dict(t)
        if ds == dt:
            return True
        else:
            return False


        