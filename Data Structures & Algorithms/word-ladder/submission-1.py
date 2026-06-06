class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 1
        
        word_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                word_map[pattern].append(word)

        q = deque([beginWord])
        seen = set()

        while q:
            q_len = len(q)

            for _ in range(q_len):
                word = q.popleft()

                print(word)
                if word == endWord: 
                    return res

                # find pattern for word
                for w in range(len(word)):
                    print('w: ', w)
                    pattern = word[:w] + '*' + word[w+1:]
                    print('pattern: ', pattern)
                    print(word_map[pattern])
                    for try_word in word_map[pattern]:
                        if try_word not in seen: 
                            seen.add(try_word)
                            q.append(try_word)

            res += 1

        return 0