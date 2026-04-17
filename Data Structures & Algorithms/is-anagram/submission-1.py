from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        c1, c2 = Counter(s), Counter(t)
        return c1 == c2
        

        