from collections import deque

def nested(nestedlist)->int:

    depth = 0
    out = 0

    qu = deque()
    qu.append(nestedlist)

    while qu:

        li = list(qu)
        for elem in li:
            qu.popleft()
            if type(elem) == int:
                out += depth*elem
            else:
                qu.extend(elem)

        depth += 1
        
    return out 


nl = [[1,1],2,[1,1]]
#nl = [1,[4,[6]]]
nl = [[[[[2]]]],1]

print(nested(nl))