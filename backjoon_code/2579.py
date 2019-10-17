n = int(input())
stair = []
_sum = []

for i in range(n):
    stair.append(int(input()))

_sum.append(stair[0])
_sum.append(stair[0]+stair[1])
_sum.append(max(stair[0], stair[1]) + stair[2])

for j in range(3,n):
    _sum.append(max(_sum[j-3]+stair[j-1]+stair[j], _sum[j-2]+stair[j]))

print(_sum[n-1])
