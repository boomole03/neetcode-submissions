class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = [0] * 26
        for s in s1:
            s1_dict[ord('a') - ord(s.lower())] += 1

        window = [0] * 26
        for r in range(len(s1)):
            window[ord('a') - ord(s2[r].lower())] += 1
            
        r = len(s1)
        while r < len(s2):
            if window == s1_dict:
                return True

            # remove left first
            window[ord('a') - ord(s2[r - len(s1)].lower())] -= 1
            
            # keep extending to the right
            window[ord('a') - ord(s2[r].lower())] += 1
            r += 1

        return window == s1_dict