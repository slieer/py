import json

# fmt: off
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
# fmt: on

jsonstr = json.dumps(j, sort_keys=True)
print("打印json字符串:%s" % jsonstr)

data2 = json.dumps(
    {"a": "Runoob", "b": 7}, sort_keys=True, indent=4, separators=(",", ": ")
)
print(data2)

print(j["a"])
print(j["arr"])

for val in j:
    print(j[val])


import json

jsonData = """{
     "a":1,
     "b":2,
     "c":3,
     "d":4,
     "e":5
}
"""
text = json.loads(jsonData)
print(text)
