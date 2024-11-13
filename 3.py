class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Define hash map
        hash_map = {}
        # Define queue
        queue = []
        # Define max sequence
        max_seq = 0

        # Iterate over the string
        for char in s: 
            # If not yet on hash map
            if char not in hash_map:
                # Store letter on a queue
                queue.append(char)
                # Store position in a hash map
                hash_map[char] = len(queue)-1
            # If already present
            else:
                # Pop until position
                aux_char = queue.pop(0)
                while aux_char != char:
                    del hash_map[aux_char]
                    aux_char = queue.pop(0)
                # Insert at queue
                queue.append(char)
                # Update hash
                hash_map[char] = len(queue)-1

            # Compare max size
            if max_seq < len(queue):
                max_seq = len(queue)

        # Return
        return max_seq



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hasht = {}
        left = 0
        right = 0
        k = 0

        while right < len(s):
            while s[right] in hasht:
                del hasht[s[left]]
                left += 1

            hasht[s[right]] = 1
            k = max(k,len(hasht))
            right += 1
        
        return k