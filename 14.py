class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        init = 0
        while init < len(strs[0]):
            count = 0
            potential_prefix = strs[0][init]

            for element in strs:
                if init >= len(element):
                    break
                elif element[init] != potential_prefix:
                    init = len(strs[0])
                else:
                    count+=1
            init += 1
            if count == len(strs):
                prefix += potential_prefix
        return prefix
            