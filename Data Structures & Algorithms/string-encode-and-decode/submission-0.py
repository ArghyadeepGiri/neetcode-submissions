class Solution:
    def __init__(self):
        self.out_str = ""
        self.out = []
        self.lengths = []

    def encode(self, strs: List[str]) -> str:
        for s in strs:
            self.out_str += s
            self.lengths.append(len(s))
        return self.out_str

    def decode(self, s: str) -> List[str]:
        start = 0
        for l in self.lengths:
            end = start + l
            self.out.append(self.out_str[start:end])
            start = end
        return self.out