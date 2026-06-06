class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs: 
            word_dict = [0] * 26
            for l in s: 
                index = ord(l) - ord('a')
                word_dict[index] += 1

            if tuple(word_dict) in d:
                d[tuple(word_dict)].append(s)
            else: 
                d[tuple(word_dict)] = [s]
        
        return list(d.values())