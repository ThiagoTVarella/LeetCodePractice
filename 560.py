class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Cumulative sum hash
        hmap = {0:1}
        cumsum = 0
        count = 0

        for elem in nums:
            cumsum += elem

            if cumsum - k in hmap:
                count += hmap[cumsum-k]

            if cumsum in hmap:
                hmap[cumsum] += 1
            else:
                hmap[cumsum] = 1

        return count

