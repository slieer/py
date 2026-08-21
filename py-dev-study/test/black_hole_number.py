"""
在数学中，黑洞数字（也称为卡普雷卡尔常数，Kaprekar's constant）
是指通过特定重复操作后，一个数字序列最终会收敛到的固定值。
"""

from random import Random
r = Random()
while True:
    a = r.randint(100, 1000)
    a_ = str(a)
    a_Len = len(a_)
    if len(set(list(a_))) == a_Len:
        break
print(f"初始值:{a}")
a = 875
result = 1
while True:
    aStr = str(a)
    aArr = list(aStr)
    aArr.sort(reverse= True)
    aMax = int(''.join(map(str, aArr)))
    print(aMax)

    aArr.sort()
    aMin = int(''.join(map(str, aArr)))
    tempVal = aMax - aMin
    if tempVal != result:
        result = tempVal
        a = tempVal
    else:
        print(f"最终结果:{tempVal}")
        break

