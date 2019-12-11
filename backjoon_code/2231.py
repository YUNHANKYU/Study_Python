n = int(input())
result =0
for i in range(1, n+1):
    copy = list(map(int, str(i)))
    result = i + sum(copy)
    if result == n:
        break
if i == n :
    print("0")
else:
    print(i)
    
