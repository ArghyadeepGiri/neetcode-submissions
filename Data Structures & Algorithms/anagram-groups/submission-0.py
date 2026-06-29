from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        temp = [0]*26
        d = {}
        for idx, st in enumerate(strs):
            for ch in st:
                elem = ord(ch) - 97
                temp[elem] += 1
            temp_str = str(temp)
            if temp_str in d:
                d[temp_str].append(idx)
            else:
                d[temp_str] = [idx]
            temp = [0]*26

        for _, value in d.items():
            output.append([strs[x] for x in value])

        return output
            

        