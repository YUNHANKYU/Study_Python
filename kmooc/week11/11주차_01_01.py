import random

def select_item(list, n):
    result=random.sample(list, n)
    return result

r = select_item([1,3,5,7,11,15,21], 5)
print(r)

t = tuple(r)
print(t)

t1 = list(zip(r, "Kmooc"))
print(t1)
