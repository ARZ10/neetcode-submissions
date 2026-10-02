from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = list(s)

        for index, char in enumerate(s):
            if char in punctuation or char.isspace():
                s[index] = ""
        s = "".join(s)
        s = s.lower()

        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True
        