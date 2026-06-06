class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isTheSame(x, y):
            if x.lower() == y.lower():
                return True
            else:
                return False
        l, r = 0, len(s) -1
        while l < r:
            if (not s[l].isalnum()):
                l +=1 
                continue
            if (not s[r].isalnum()):
                r -= 1
                continue
            
            if isTheSame(s[l], s[r]):
                l += 1
                r -= 1
            else: 
                return False

        return True