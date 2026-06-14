class Solution:
    def isValid(self, s: str) -> bool:
        # create dict for mapping
        par_dict = {'}': '{', ')': '(', ']': '['}
        have = []
        for r in s: 
            # if we have a open parentheses
            if r not in par_dict:
                have.append(r)
            elif not have or have.pop() != par_dict[r]:
                return False 
        return not have