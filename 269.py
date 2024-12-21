class Node():
  def __init__(self,char,neighbors=[],parents=[]):
    self.char = char
    self.neighbors = neighbors
    self.parents = parents

def diff_prefix(str1,str2):
  n = min(len(str1),len(str2))
  i = 0
  while i < n and str1[i] == str2[i]:
    i += 1
  if i == n:
    return None 
  else:
    return (str1[i],str2[i])

def create_graph(edges):
  created = {}
  for i,j in edges:
    if i not in created: 
      i_node = Node(i,[],[])
      created[i] = i_node
    
    if j not in created: 
      j_node = Node(j,[],[])
      created[j] = j_node
    
    created[i].neighbors.append(created[j])
    created[j].parents.append(created[i])

  roots = []
  for char in created.keys():
    if created[char].parents == []:
        roots.append(created[char])

  return roots

def post_traversal(roots, visited, order):

  if not roots:
    return order,visited
  
  if not roots[0].neighbors:
    return roots[0].char + order, visited
  
  for root in roots:
    for node in root.neighbors:
      if node not in visited:
        visited.add(node)
        order,visited = post_traversal([node],visited,order)
    order = root.char + order

  return order, visited
  
def alien_order(words: list[str]) -> str:
    
  edges = []
  for i in range(len(words)-1):
    edges.append(diff_prefix(words[i],words[i+1]))

  roots = create_graph(edges)

  visited = set()
  order = ''
  order, visited = post_traversal(roots, visited, order)

  return order

words = ['bs', 'dsb', 'dbs']
words = ["wrt", "wrf", "er", "ett", "rftt"]
order = alien_order(words)
print(order)
