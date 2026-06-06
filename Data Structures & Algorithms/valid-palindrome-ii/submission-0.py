class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isTheSame(x, y):
            while x < y:
                if s[x] == s[y]: 
                    x += 1
                    y -= 1
                else: 
                    return False
            return True

        l, r = 0, len(s) -1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isTheSame(l + 1, r) or isTheSame(l, r - 1)
                
        return True
        