arr = []
result = [0,0,0]

def tree(n, y, x):
    if n == 1:
        result[int(arr[y][x])] += 1
        return
    minus = True
    zero = True
    one = True
    for i in range(y, n+y):
        for j in range(x, n+x):
            if arr[i][j] == '2':
                zero = False
                one = False
            elif arr[i][j] == '0':
                minus = False
                one = False
            else:
                minus = False
                zero = False
    if minus:
        result[2] += 1
    elif zero:
        result[0] += 1
    elif one:
        result[1] += 1
    else:
        tree(int(n/3), y, x)
        tree(int(n/3), y, x+int(n/3))
        tree(int(n/3), y, x+2*int(n/3))
        
        tree(int(n/3), y+int(n/3), x)
        tree(int(n/3), y+int(n/3), x+int(n/3))
        tree(int(n/3), y+int(n/3), x+2*int(n/3))
        
        tree(int(n/3), y+2*int(n/3), x)
        tree(int(n/3), y+2*int(n/3), x+int(n/3))
        tree(int(n/3), y+2*int(n/3), x+2*int(n/3))

n = int(input())

if (n % 3) != 0:
    print("It's not power of 3")

for i in range(n):
    arr.append(list(input().replace('-1', '2').replace(' ', '')))

tree(n, 0, 0)

print(result[2])
print(result[0])
print(result[1])

