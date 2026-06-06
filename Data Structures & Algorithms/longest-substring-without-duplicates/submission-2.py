class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set() 
        l, r = 0, 0
        res = 0

        #s = "zxyzxyz"
        #.    l  r
        while r < len(s):
            while r < len(s) and  s[r] not in seen: 
                seen.add(s[r])
                r += 1
            res = max(res, r - l)

            while  r < len(s) and l <= r and s[r] in seen: 
                seen.remove(s[l])
                l +=1


        return res