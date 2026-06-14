class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        1) create dict of t
        2) create running dict for the window
        3) some way to track when window is valid
        4) minimize until its no longer valid
        """

        t_dict = Counter(t)
        w_dict = defaultdict(int)
        matches = len(t_dict)
        seen = 0

        res = [float('inf'), ""] 
        l = r = 0

        while r < len(s):
            # extend via the r point
            w_dict[s[r]] += 1

            # if the count matches, let's increase seen
            if w_dict[s[r]] == t_dict[s[r]]:
                seen += 1

            # we have seen enough to have a valid substring
            while seen == matches:
                # let's update the result and keep reducing the window
    
                # is it worth updating result
                if (r - l + 1) < res[0]:
                    res = [(r-l+1), s[l:r+1]]

                # we need to update the seen, based on the left pointer
                if w_dict[s[l]] == t_dict[s[l]]:
                    seen -= 1

                # update the substring
                w_dict[s[l]] -= 1 
                l +=1             

            r +=1    

        return res[1]