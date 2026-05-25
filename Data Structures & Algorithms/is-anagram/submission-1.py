class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        slist.sort()
        tlist = list(t)
        tlist.sort()
        if slist == tlist:
            return True
        else : 
            return False
