class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Input: s = "OUZODYXAZV", t = "XYZ"

        Output: "YXAZ"
        """

        if t == "":
            return ""
        
        dict_t = defaultdict(int)
        for st in t:
            dict_t[st] += 1

        have, need = 0, len(dict_t)
        window = defaultdict(int)

        res, resLen = [-1, - 1], float("inf") 
        l = 0 
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in dict_t and window[c] == dict_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    # new result
                    res = [l , r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in dict_t and window[s[l]] < dict_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l : r + 1] if resLen != float("inf") else ""