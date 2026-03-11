class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        occurrences = []
        invalid = False
        size = len(haystack)
        for i, h in enumerate(haystack):
            if h == needle[0]:
                occurrences.append(i)
        if len(needle) > 1:
            for o in occurrences:
                invalid = False
                for j, n in enumerate(needle[1:]):
                    if (o+j+1) >= size or haystack [o+j+1] != n:
                        invalid = True
                        break
                else:
                    return o
        
        if not occurrences or invalid:
            return -1
        else:
            return occurrences[0]


# time complexity O(m * n)
print(Solution.strStr(Solution,"leetcode", "leeto"))