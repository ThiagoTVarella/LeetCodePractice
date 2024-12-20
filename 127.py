from collections import deque, defaultdict

diff_count = lambda s1,s2: sum(c1 != c2 for c1,c2 in zip(s1,s2))

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        adjacency = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                adjacency[pattern].append(word)

        # Start with beingWord on queue
        queue = deque([(beginWord,1)])
        visited = set()

        while queue:
            new_word,count = queue.popleft()
            for i in range(len(new_word)):
                new_pattern = new_word[:i]+'*'+new_word[i+1:]
                if new_pattern in adjacency:
                    neighbors = adjacency[new_pattern]
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            if neighbor == endWord:
                                return count+1
                            queue.append((neighbor,count+1))
                            visited.add(neighbor)

            # for word in wordList:
            #     if word not in visited and diff_count(new_word,word) == 1:
            #         if word == endWord:
            #             return count+1
            #         queue.append((word,count+1))
            #         visited.add(word)

        return 0
        # check each word from wordList
        # if it wasn't used yet and it differs by only one letter, append to queue
        
        # add count
        # if we reached endword, return count
