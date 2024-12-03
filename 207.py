from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        n_preqs = {}
        enables = {}

        for prerequisite in prerequisites:
            n_preqs[prerequisite[0]] = n_preqs.get(prerequisite[0],0)+1
            
            if prerequisite[1] not in enables:
                enables[prerequisite[1]] = set([prerequisite[0]])
            else:
                enables[prerequisite[1]].add(prerequisite[0])

        queue = deque([])
        visited = set()

        for course in range(numCourses):
            if course not in n_preqs:
                queue.append(course)
                visited.add(course)
        
        while queue:
            course = queue.popleft()
            
            if course in enables:
                for new_course in enables[course]:
                    n_preqs[new_course] -= 1
                    if n_preqs[new_course] == 0: 
                        del n_preqs[new_course]
                        queue.append(new_course)
                        visited.add(new_course)

        if len(visited) != numCourses: return False
        else: return True