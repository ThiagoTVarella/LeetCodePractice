# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        if isBadVersion(0):
            return 1

        lastgood = 1
        firstbad = n

        while lastgood < firstbad:
            
            mid = lastgood + (firstbad-lastgood)//2

            if isBadVersion(mid):
                firstbad = mid
            else:
                lastgood = mid+1
            
        return firstbad

