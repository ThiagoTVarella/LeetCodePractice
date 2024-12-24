from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        dict_to_group = defaultdict(list)

        for word in strings:
            ref = word[0]
            key = []
            for ch in word:
                key_n = ord(ch)-ord(ref)
                if key_n < 0:
                    key_n += 26
                key.append(key_n)
            dict_to_group[tuple(key)].append(word)

        return list(dict_to_group.values())