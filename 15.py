class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        h = {}
        for i,elem in enumerate(nums):
            h[elem] = i

        triplets = set()

        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                cumm = -nums[i]-nums[j]
                if cumm in h and h[cumm] > j:
                    s_t = tuple(sorted([nums[i],nums[j],nums[h[cumm]]]))
                    triplets.add(s_t)

                    # elif s_ts[s_t[0]] != s_t[1]:
                    #     s_ts[s_t[0]] = s_t[1]
                    #     triplets.append(s_t)
            if nums[i] in h:
                del h[nums[i]]
        
        return [list(trip) for trip in triplets]