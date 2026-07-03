class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False
        occ_s, occ_t = {}, {}
        for i in range(len(s)):
            
            if s[i] not in occ_s:
                occ_s[s[i]] = 0
            occ_s[s[i]] += 1
            
            if t[i] not in occ_t:
                occ_t[t[i]] = 0
            occ_t[t[i]] += 1
        
        s_set = set([c for c in s])
        for c in s_set:
            if occ_s != occ_t:
                return False
        return True