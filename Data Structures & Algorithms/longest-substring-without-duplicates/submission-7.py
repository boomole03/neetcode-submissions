class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        res = 0

        for r, c in enumerate(s):
            # we need to update l pointer
            if c in seen and seen[c] >= l:
                l = seen[c] + 1

            seen[c] = r
            res = max(r - l + 1, res)

        return res