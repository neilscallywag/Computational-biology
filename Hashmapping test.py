words = ["hello", "goodbye", "hi", "how are you", "hi"]
keys = ["a", "b", "c", "d", "e"]
from itertools import zip_longest

def hashmap(keys, pair):
        return hashmap_helper(list(set(keys)),list(set(pair)))

def hashmap_helper(keys,pair):
        for key in range(len(keys)):
                         if len(keys) != len(pair):
                                 table = {}
                                 table = dict(zip_longest(table[keys[key]], pair[key]))
        return table
         
                
                

                
print(hashmap(keys, words))
 
