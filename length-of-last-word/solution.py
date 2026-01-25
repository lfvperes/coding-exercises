class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_char = -1
        for i in range(len(s)-1, -1, -1):
            print(i)
            if last_char == -1:
                if s[i] != ' ':
                    last_char = i
            else:
                if s[i] == ' ':
                    return last_char - i
                if i == 0:
                    return last_char + 1 
        else:
            return last_char + 1