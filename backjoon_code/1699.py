import math

n = int(input())
_input = n
n_sqrt = int(math.sqrt(n))
_min = n
result =0

while n_sqrt:
    temp = n_sqrt
    while True:
        n = n - pow(temp, 2)
        if n == 0:
            result = result + 1
            break
        elif n > 0:
            result = result + 1
            temp = int(math.sqrt(n))
        else:
            print("error")
            exit()
    if result > 4:
        n_sqrt = n_sqrt - 1
        result = 0
        n = _input
    else:
        if _min > result:
            _min = result
        n_sqrt = n_sqrt - 1
        result = 0
        n = _input
print(_min)
