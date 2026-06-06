class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        
        s1_counter, s2_counter = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_counter[ord(s1[i])- ord('a')] += 1
            s2_counter[ord(s2[i])- ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1_counter[i] == s2_counter[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                # if we have seen all chars then just return True
                return True

            index = ord(s2[r]) - ord('a')
            s2_counter[index] += 1
            if s1_counter[index] == s2_counter[index]:
                matches += 1
            elif s1_counter[index] + 1 == s2_counter[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2_counter[index] -= 1
            if s1_counter[index] == s2_counter[index]:
                matches += 1
            elif s1_counter[index] - 1 == s2_counter[index]:
                matches -= 1
            l += 1
        return matches == 26


















        