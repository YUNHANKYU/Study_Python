count=0
a = []
    
n, k = map(int, input().split(' '))
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)

for i in range(n):
    count += int(k / a[i])
    k = k % a[i]

print(count)
