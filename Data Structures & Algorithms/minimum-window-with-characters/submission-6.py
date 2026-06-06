class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: 
            return ''

    
        res = "", float('inf')
        dict_t = defaultdict(int)
        for i in t: 
            dict_t[i] +=1

        matches = len(dict_t) # keep track of the correct values we have seen
        formed = 0 
        l, r = 0, 0

        dict_s = defaultdict(int)
        while r < len(s):
            if s[r] in dict_t: 
                dict_s[s[r]] +=1
                if dict_s[s[r]] == dict_t[s[r]]: 
                    formed +=1 
                
            # check matches if equal to zero
            while matches == formed: 
                sub = s[l:r+1]
                if len(sub) <  res[1]:
                    res = sub, len(sub)

                if s[l] in dict_t:
                    if dict_s[s[l]] == dict_t[s[l]]:
                        formed -=1
                    dict_s[s[l]] -=1
                l += 1

            r +=1 



        return res[0] if res[1] != float('inf') else ""
