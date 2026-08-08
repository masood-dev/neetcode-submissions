class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this is neat, but trades both time and space for one-liner
        return sorted(s) == sorted(t)