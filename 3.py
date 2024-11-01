class Solution:
    def Node(self,key):
        self.key = key
        self.next = None


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
