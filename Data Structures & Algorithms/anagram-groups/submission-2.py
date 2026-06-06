class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - make a counter for each word in the list
        - use the count as a key and add words that matcht that count
        """
        dic = defaultdict(list)
        for s in strs:
            t = [0] * 26
            for i in s: 
                idx = ord(i) - ord('a')
                t[idx] +=1
            
            dic[tuple(t)].append(s)

        print('dictionary: ', dic.values())
        return [ i for i in dic.values()]
