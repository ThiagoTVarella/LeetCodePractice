class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        pt_1, pt_2 = 0,len(numbers)-1

        while (soma := numbers[pt_1] + numbers[pt_2]) != target:
            if soma > target:
                pt_2 -= 1
            if soma < target:
                pt_1 += 1
        
        return [pt_1+1,pt_2+1]