class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_dict = [0] * 26
        w_dict = [0] * 26

        for i in range(len(s1)):
            s1_dict[ord(s1[i]) - ord('a')] += 1
            w_dict[ord(s2[i]) - ord('a')] += 1

        r = len(s1)

        while r < len(s2):
            if s1_dict == w_dict:
                return True

            # remove left
            w_dict[ord(s2[r - len(s1)]) - ord('a')] -= 1

            # add right
            w_dict[ord(s2[r]) - ord('a')] += 1

            r += 1

        return s1_dict == w_dict