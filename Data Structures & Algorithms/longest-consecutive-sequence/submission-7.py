class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        turn the array into a set

        # loop through the set starting from the lowest item

        """
        

        num_set = set(nums)

        res = 0
        for i in num_set: 
            if (i - 1) not in num_set: 
                curr = 1
                while (i + curr) in num_set: 
                    curr += 1
                res = max(curr, res)
        return res