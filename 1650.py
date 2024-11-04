left = lambda pos: 2*pos + 1
right = lambda pos: 2*pos + 2
parent = lambda pos: (pos-1)//2

def lowestCommonAncestor(root, p: int, q: int) -> int:

    binn = {}
    binn[root[0]] = ''
    for i in range(1,len(root),2):

        binn[root[i]] = binn[root[parent(i)]]+'0'
        if i+1 < len(root):
            binn[root[i+1]] = binn[root[parent(i)]]+'1'

    # Store the element and its binned representation

    # Find binn of p and q
    binnp = binn[p]
    binnq = binn[q]

    # Get common
    common = ''
    k = min(len(binnp),len(binnq))
    i = 0
    while i < k and binnp[i] == binnq[i]:
        common += binnp[i]
        i += 1
    
    # Navigate tree
    start = 0
    for elem in common:
        if elem == '0':
            start = left(start)
        else:
            start = right(start)

    return root[start]
 
root = [3,5,1,6,2,0,8,None,None,7,4]

print(lowestCommonAncestor(root, 5,4))