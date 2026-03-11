class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        carry = 0
        n_a = len(a)
        n_b = len(b)
        n = max(n_a, n_b)
        if n_a > n_b:
            b = "0" * (n_a - n_b) + b
        elif n_a < n_b:
            a = "0" * (n_b - n_a) + a
        
        for i in range(n-1, -1, -1):
            s = int(a[i]) + int(b[i]) + carry
            bit = s % 2
            carry = s // 2
            c = str(bit) + c
        if carry == 1:
            c = "1" + c
        return c