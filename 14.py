class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = ''
        # init = 0
        # while init < len(strs[0]):
        #     count = 0
        #     potential_prefix = strs[0][init]

        #     for element in strs:
        #         if init >= len(element):
        #             break
        #         elif element[init] != potential_prefix:
        #             init = len(strs[0])
        #         else:
        #             count+=1
        #     init += 1
        #     if count == len(strs):
        #         prefix += potential_prefix
        # return prefix
            
        prefix = ''
        strs = sorted(strs)
        position = 0
        first = strs[0]
        last = strs[-1]
        for position in range(min(len(first),len(last))):
            if first[position] == last[position]:
                prefix += first[position]
            else:
                return prefix
        return prefix