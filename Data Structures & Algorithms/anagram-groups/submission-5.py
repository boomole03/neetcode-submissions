class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for st in strs: 
            chars = [0] * 26
            for s in st: 
                i = ord(s) - ord('a')
                chars[i] += 1

            d[tuple(chars)].append(st)
        
        return [d[n] for n in d]