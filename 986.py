class Solution:

    def intersect(self,list1,list2):
        lo = max(list1[0],list2[0])
        hi = min(list1[1],list2[1])
        if lo <= hi:
            return [lo,hi]
        else:
            return []

    def before(self,list1,list2):
        if list1[1] < list2[0]:
            return True
        else:
            return False


    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        if not firstList or not secondList:
            return []

        pt1 = 0
        pt2 = 0
        output = []

        while pt1 < len(firstList) and firstList[pt1][1] < secondList[pt2][0]:
            pt1 += 1

        while pt1 < len(firstList) and pt2 < len(secondList):

            if (inter := self.intersect(firstList[pt1],secondList[pt2])):
                output.append(inter)

            if secondList[pt2][1] < firstList[pt1][1]:
                pt2 += 1
            else:
                pt1 += 1

        return output




        # output = []

        # for list1 in firstList:
        #     for list2 in secondList:
        #         if (inter := self.intersect(list1,list2)):
        #             output.append(inter)
        
        # return output
