class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        bracket_pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        bracket_stack = []
        for b in s:
            if b == '(' or b == '{' or b == '[':
                bracket_stack.append(b)
            elif b == ')' or b == '}' or b == ']':
                if len(bracket_stack) == 0:
                    return False
                if bracket_stack[-1] == bracket_pairs[b]:
                    bracket_stack.pop()
                else:
                    return False
        if len(bracket_stack) > 0:
            return False
        
        return True