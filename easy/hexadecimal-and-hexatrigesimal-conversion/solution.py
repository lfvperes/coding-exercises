class Solution:
    def concatHex36(self, n: int) -> str:
        return self.convert_to_base(n**2, 16) + self.convert_to_base(n**3, 36)
        
    def convert_to_base(self, n, base):
        result = ""
        while (n > 0):
            temp = n % base
            temp += 48 if temp < 10 else 55
            result = chr(temp) + result
            n //= base
        return result