class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = Counter(s1)
        window = defaultdict(int)
        l = 0

        for r in range(len(s1)):
            window[s2[r]] += 1

        # check the first window
        if window == s1_dict:
            return True
        r = len(s1)
        while r < len(s2):
            print(window)
            # remove left first
            window[s2[l]] -= 1
            if window[s2[l]] == 0: 
                del window[s2[l]]
            
            # keep extending to the right
            window[s2[r]] += 1

            if window == s1_dict:
                return True

            r += 1
            l +=1 

        return False
            