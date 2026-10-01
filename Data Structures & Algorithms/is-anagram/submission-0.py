class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s, t = s.lower(), t.lower()
        s = list(s)

        try:
            for char in t:
                s.remove(char)
        except ValueError:
            return False

        return len(s) == 0


        