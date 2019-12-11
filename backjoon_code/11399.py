n = int(input())
nTimes = list(map(int, input().split()))
result = 0
nTimes.sort()

for i in range(n):
    result += nTimes[i] * (n-i)

print(result)
