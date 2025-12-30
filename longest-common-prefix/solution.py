from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size_smallest_word = len(strs[0])
        index_smallest_word = 0
        for idx, word in enumerate(strs):
            if len(word) < size_smallest_word:
                size_smallest_word = len(word)
                index_smallest_word = idx

        current_prefix = ""
        for i, c in enumerate(strs[index_smallest_word]):
            for s in strs:
                if s[i] == c:
                    pass
                else:
                    return current_prefix
            current_prefix += c
        return current_prefix
