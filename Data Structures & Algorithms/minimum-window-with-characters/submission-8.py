class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        res = (float('inf'), "")

        t_count = Counter(t)
        window = defaultdict(int)

        matches = 0
        required = len(t_count)

        l = r = 0

        while r < len(s):
            # grow window to the right
            window[s[r]] += 1

            if t_count[s[r]] and t_count[s[r]] == window[s[r]]:
                matches += 1

            # check if we have a window that is valid
            print(matches, ' vs ', required)
            while matches == required:
                # let update our res, maybe
                print('old res: ', res[0], ' ', (r - l + 1))
                if res[0] > (r - l + 1):
                    print('New res')
                    res = ((r-l+1), s[l:r+1])

                # now left remove from the left
                if t_count[s[l]] and t_count[s[l]] == window[s[l]]:
                    matches -= 1

                window[s[l]] -= 1
                l += 1
                
            r +=1 

        return res[1]