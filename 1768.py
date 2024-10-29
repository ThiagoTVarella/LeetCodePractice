class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        pointer_1 = 0
        pointer_2 = 0

        len1 = len(word1)
        len2 = len(word2)

        keep_going = True
        while keep_going:
            merged+=word1[pointer_1]
            merged+=word2[pointer_2]
            pointer_1 += 1
            pointer_2 += 1

            if pointer_1 >= len1:
                keep_going = False
                while pointer_2 < len2:
                    merged+=word2[pointer_2]
                    pointer_2 += 1
            elif pointer_2 >= len2:
                keep_going = False
                while pointer_1 < len1:
                    merged+=word1[pointer_1]
                    pointer_1 += 1
        return merged
