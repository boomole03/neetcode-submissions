class Solution:
    def isValid(self, s: str) -> bool:
        # create dict for mapping
        par_dict = {'}': '{', ')': '(', ']': '['}
        have = []
        for r in s: 
            # if we have a open parentheses
            if r in '[({':
                have.append(r)
            else:
                # does the close match the latest open
                if not have or have[-1] != par_dict[r]:
                    return False
                else: 
                    have.pop()
        return True if not have else False