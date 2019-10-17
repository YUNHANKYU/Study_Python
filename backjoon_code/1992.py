arr = []

def quad_tree(n, y, x):
    if n == 1:
        print(arr[y][x], end='')
        return
    zero = True
    one = True
    for i in range(y, n+y):
        for j in range(x, n+x):
            if arr[i][j] == '1':
                zero = False
            else:
                one = False
    if one:
        print("1", end='')
    elif zero:
        print("0", end='')
    else:
        print("(", end='')
        quad_tree(int(n/2), y, x)
        quad_tree(int(n/2), y, x+int(n/2))
        quad_tree(int(n/2), y+int(n/2), x)
        quad_tree(int(n/2), y+int(n/2), x+int(n/2))
        print(")", end='')

n = int(input())

if (n & (n-1)) != 0:
    print("It's not power of 2")

for i in range(n):
    arr.append(list(input()))

quad_tree(n, 0, 0)

