class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this is the same kind of question nasrin asked i can't solve.
        # here don't knowing the indexing and dict properties is a minus
        # time complexity is O(n + m), slightly better than previous one
        if len(s) != len(t):
            return False
            
        count_s,  count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t