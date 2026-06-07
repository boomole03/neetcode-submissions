class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_dict = defaultdict(list)

        for st in strs:
            idx = [0] * 26
            for s in st:
                idx[ord(s) - ord('a')] +=1

            an_dict[tuple(idx)].append(st)

        print(an_dict.values())
        return [ i for i in an_dict.values()]