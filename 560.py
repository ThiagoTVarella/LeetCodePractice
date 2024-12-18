class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = count = 0
        prefix_dict = {0:1}

        for elem in nums:

            prefix_sum += elem

            if prefix_sum-k in prefix_dict: count += prefix_dict[prefix_sum-k]

            prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum,0)+1

        return count




        # prefix_dict = {0:1}
        # prefix_sum = 0
        # count = 0

        # for elem in nums:
        #     prefix_sum += elem
        #     if prefix_sum-k in prefix_dict:
        #         count += prefix_dict[prefix_sum-k]
        #     prefix_dict[prefix_sum] = prefix_dict.setdefault(prefix_sum,0)+1
        
        # return count

















        # prefix_sum = {0:1}
        # cumsum = 0
        # count = 0

        # for elem in nums:
            
        #     cumsum += elem

        #     # check if cumsum - k is in prefix_sum
        #     if cumsum - k in prefix_sum:

        #         # if yes, add the hash value to count
        #         count += prefix_sum[cumsum-k]

        #     prefix_sum[cumsum] = prefix_sum.get(cumsum,0)+1         

        # return count




        # # # hash of cumulative sum. initialize with 0
        # # hashcumm = {0:1}

        # # # count
        # # count = 0

        # # # cumsum
        # # cumsum = 0

        # # # iterate over nums
        # # for elem in nums:

        # #     # calculate cumsum
        # #     cumsum += elem

        # #     # check if difference between cumsum and k is in hash
        # #     if cumsum - k in hashcumm:

        # #         # increase count
        # #         count += hashcumm[cumsum-k]

        # #     # Store in map
        # #     if cumsum in hashcumm:
        # #         hashcumm[cumsum] += 1
        # #     else:
        # #         hashcumm[cumsum] = 1
        
        # # # return
        # # return count