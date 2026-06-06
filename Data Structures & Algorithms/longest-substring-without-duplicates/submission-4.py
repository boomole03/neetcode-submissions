class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        find the length of the longest substring without duplicates
        """

        seen = set()
        res = 0
        l = 0
        for i in s:
            if i in seen: 
                while i in seen:
                    if s[l] in seen:
                        seen.remove(s[l])
                    l += 1
                seen.add(i)
            else: 
                seen.add(i)
                res = max(res, len(seen))
        return res