class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs: 
            word_counter = [0] * 26
            for char in word: 
                idx = ord('a') - ord(char.lower())  
                word_counter[idx] += 1
            
            groups[tuple(word_counter)].append(word)
        return [groups[n] for n in groups]