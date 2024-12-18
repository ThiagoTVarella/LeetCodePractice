class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isWord = False

class Solution:

    def create_trie(self,wordDict):

        root = TrieNode()

        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.chars:
                    curr.chars[ch] = TrieNode()
                curr = curr.chars[ch]
            curr.isWord = True

        return root


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        trie = self.create_trie(wordDict)

        @cache
        def check_word(index,node):

            if index == len(s):
                return node.isWord

            # check if index can continue in trie
            if s[index] in node.chars and check_word(index+1, node.chars[s[index]]): return True
            # check if index start again
            if node.isWord and check_word(index,trie): return True            

            return False

        return check_word(0,trie)


        # 0, trie:
        # a0 in node.chars and:
            # a1 in node.chars and
                # a2 in node.chars and
                    # a3 in node.chars and
                        # a4 node in node.chars, but it is word
                        # so check if a4 in trie













        # # Memorized recursion
        # # for each word, I check if the string left starts with word
        # # if it does, check if the recursion works on the remaining word or if'ts the end

        # @cache
        # def check_word(partial_string):
            
        #     for word in wordDict:
        #         if partial_string.startswith(word):
        #             substring = partial_string[len(word):]
        #             if check_word(substring) or partial_string == word:
        #                 return True

        #     return False

        # return check_word(s)

























        # @cache
        # def check_word(subword):
        #     for word in wordDict:
        #         if subword.startswith(word):
        #             substring = subword[len(word):]
        #             if (check_word(substring) or subword == word):
        #                 return True
        #     return False
        
        # return check_word(s)


# class TrieNode:
#     def __init__(self):
#         # TrieNode has chars dict and isWord flag
#         self.chars = {}
#         self.isWord = False

# class Solution:

#     def create_trie(self, wordDict):
#         # To create a trie, we start with a root
#         trie = TrieNode()
#         # iterate through the words. In the beginning, set current at root
#         for word in wordDict:
#             currNode = trie
#             # for each letter, check if letter is in the chars of the current node
#             for ch in word:
#                 if ch not in currNode.chars:
#                     # if it isnt, create trie node for that letter 
#                     currNode.chars[ch] = TrieNode()
#                 # set next current as the node of that letter
#                 currNode = currNode.chars[ch]
#             # after the letters, set isWord to True
#             currNode.isWord = True

#         return trie

#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

#         # Create trie from dict
#         trie = self.create_trie(wordDict) # O(m*k) time and space

#         # Memoize to save time in specific cases
#         @cache
#         def can_make_word(i, node):

#             # Base case when we reach the end of s
#             if i == len(s):
#                 return node.isWord

#             # Check if the current letter continues the word in the trie
#             if s[i] in node.chars and can_make_word(i+1, node.chars[s[i]]):
#                 return True

#             # Check if the current letter ends a word and if it works if the remaining of s
#             if node.isWord and can_make_word(i, trie):
#                 return True

#             return False

#         return can_make_word(0, trie)









        # # wordDict = set(wordDict)

        # dp = [0 for _ in range(len(s))]

        # queue = deque()
        # keys = wordDict

        # for key in keys:
        #     queue.append((key,0))

        # while queue:
        #     key,i = queue.popleft()
        #     if i+len(key) <= len(s) and dp[i+len(key)-1]:
        #         continue
                
        #     if i+len(key) <= len(s) and s[i:i+len(key)] == key:
        #         dp[i+len(key)-1] = 1
        #         if i+len(key) == len(s):
        #             return True
        #         for newkey in keys:
        #             if i+len(key)+len(newkey)-1 < len(s):
        #                 if not dp[i+len(key)+len(newkey)-1]:
        #                     queue.append((newkey,i+len(key)))

        # return False


        # # setdict = set(wordDict)
        # # dp = [False for i in range(len(s)+1)]
        # # dp[0] = True

        # # for i in range(1,len(s)+1):
        # #     for j in range(0,i):
        # #         if dp[j] and s[j:i] in setdict:
        # #             dp[i] = True
        # #             break

        # # return dp[-1]
