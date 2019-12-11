from copy import *

numList = [1,3,5,7,9]
numshallow = numList
numdeep = deepcopy(numList)

print("numList = ", numList)
print("numshallow = ", numshallow)
print("numdeep = ", numdeep)

numshallow.append(99)
numdeep.append(111)

print("after appending", "="*20)
print("numList = ", numList)
print("numshallow = ", numshallow)
print("numdeep = ", numdeep)
