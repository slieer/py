import json

j = {
     'a' :"b",
     'b' : "a",
     "arr" : [
              [1, 2, 34, 4],
              ['a', 'b', '']
              
              ],
     "map" : {
              "x" : 123
              }
     }

print(json.dumps(j))
"""print j["a"]

print j["arr"]"""
for val in j:
    print(j[val])
