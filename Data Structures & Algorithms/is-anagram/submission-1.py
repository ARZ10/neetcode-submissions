class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_copy, t_copy = s.lower(), t.lower()
        if len(s_copy) != len(t_copy):
            return False

        s_set, t_set = set(s_copy), set(t_copy)
        if len(s_set - t_set) != 0:
            return False
        
        s, t = s.lower(), t.lower()
        s = list(s)

        try:
            for char in t:
                s.remove(char)
        except ValueError:
            return False


        return len(s) == 0


        