class Solution:
    def create_dict(self, s):
        counts = [0] * 26
    
        # Iterate through each character in the string
        for char in s:
            # Check if the character is a lowercase ASCII letter
            if 'a' <= char <= 'z':
                # Calculate the 0-25 index using ASCII values
                index = ord(char) - ord('a')
                counts[index] += 1
                
        return counts

    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)
        if ls1 > ls2:
            return False
        s1_d = self.create_dict(s1)
        l = 0
        r = l + ls1
        while r <= ls2:
            #print(s2[l:r])
            temp_d = self.create_dict(s2[l:r])
            if temp_d == s1_d:
                return True
            l += 1
            r = l + ls1
            #print(l, r)
        return False
        


        