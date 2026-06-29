class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {')': '(',  ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != s_dict[ch]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False
        