class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            print(i)
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] += carry
                carry = 0
        return digits