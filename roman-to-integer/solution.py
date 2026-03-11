class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        translate = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        N = len(s)
        i = 0
        while i < N:
            if i < N-1 and translate[s[i]] < translate[s[i+1]]:
                result += translate[s[i+1]]-translate[s[i]]
                i += 1
            else:
                result += translate[s[i]]
            
            i += 1
        
        return result