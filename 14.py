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
            


from typing import List

def common_prefix(strs: List[str]) -> str:
    
    # Defining a prefix
    prefix = ''

    # Define common pointer
    pointer = 0

    while pointer < len(strs[0]):

        # Define potential prefix
        potential_prefix = strs[0][pointer]

        # Reset counter
        counter = 0

        # Run through strs
        for element in strs:

            # Check if pointer is in element
            if pointer < len(element):
                # Check if potential prefix
                if(element[pointer] == potential_prefix):
                    counter += 1
                else:
                    break
            else:
                break

            # Check if counter matches length of strs
            if counter == len(strs):
                prefix += potential_prefix

        pointer += 1

    return prefix

print(common_prefix(["dogsdih","do","dogcar"]))