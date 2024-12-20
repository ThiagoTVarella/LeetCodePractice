class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        count = [0]*121
        prefix_count = [0]*121
 
        # Count occurrences of each age
        for age in ages: count[age] += 1
        
        # Build prefix sum array
        for i in range(1, 121):
            prefix_count[i] = prefix_count[i - 1] + count[i]

        n_valid = 0
        for age in ages:
            lo = int(0.5 * age) + 7
            hi = age
            if lo < age:  # Only calculate if the range is valid
                n = prefix_count[hi] - prefix_count[lo] - 1  # Exclude self
                n_valid += n  # Multiply by count of current age

        return n_valid
