from collections import Counter

# array strings
# group anagrams

# ex: ["eat", "tea", "tan", "ate", "nat", "bat"]
# [[eat, tea, ate],[tan, nat],[bat]]

# biggest word has lenght k
# list has n words

# O(n*k*log(k))

def group_anagrams(words):

  # dictionary with counters
  dict_counters = {}

  # Iterate through the array words with two poitners
  word = 0
  while word < len(words):
    counter = str(sorted(words[word]))
    
    if counter in dict_counters:
      dict_counters[counter].append(word)
    else:
      dict_counters[counter] = [word]
    word += 1

  # Iterate through the keys of the dictionary,
  output = []
  keys = dict_counters.keys()
  for key in keys:
    aux_list= []
    for word in dict_counters[key]:
      aux_list.append(words[word])
    output.append(aux_list)

  return output

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

words = []
print(group_anagrams(words))

words = ["eat"]
print(group_anagrams(words))

words = ["eat", "stea", "stan", "ate", "ants", "bat"]
print(group_anagrams(words))

