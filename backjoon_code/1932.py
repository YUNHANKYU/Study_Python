n = int(input())
t = []

t.append(list(map(int, input().split())))

for i in range(1, n):
    t.append(list(map(int, input().split())))
    for j in range(i+1):
        if j == 0 and i != 0:
            t[i][j] = t[i][j] + t[i-1][j]
        elif j == i:
            t[i][j] = t[i][j] + t[i-1][j-1]
        else :
            t[i][j] = t[i][j] + max(t[i-1][j-1], t[i-1][j])

print(max(t[n-1]))
