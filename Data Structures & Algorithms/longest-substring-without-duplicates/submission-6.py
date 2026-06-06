class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = r = 0
        res = 0
        while r < len(s):
            # keep extening to the right if not in seen
            if s[r] not in seen: 
                seen.add(s[r])
                r += 1
                res = max(r - l, res)
            else:
                while l <= r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1


        return res