class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        last = None
        res = ''
        increasing = True
        while s:
            if increasing:
                smallest = None
                for j in range(len(s)):
                    c = s[j]
                    if (smallest is None or c < smallest) and (last is None or c > last):
                        smallest = c
                        ind_smallest = j
                if smallest is not None:
                    s.pop(ind_smallest)
                    last = smallest
                    res = res + smallest
                else:
                    increasing = False
                    last = None
            if not increasing:
                largest = None
                for j in range(len(s)):
                    c = s[j]
                    if (largest is None or c > largest) and (last is None or c < last):
                        largest = c
                        ind_largest = j
                if largest is not None:
                    s.pop(ind_largest)
                    last = largest
                    res = res + largest
                else:
                    increasing = True
                    last = None
        
        return res