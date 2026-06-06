class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxf = 0
        res = 0
        l = 0

        for r, char in enumerate(s):
            count[char] += 1 
            maxf = max(maxf, count[char])

            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res