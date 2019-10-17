n,w = map(int, input().split())
price = []
coin = 0

if not(n >= 1 and n <= 15) or not(w >=1 and w<= 100000):
    print("error")
    exit()

for i in range(n):
    price.append(int(input()))

for j in range(1, n):
    if coin == 0 :
        if price[j-1] < price[j] :
            #무조건 사라
            coin = coin + (w // price[j-1])
            w = w - (coin * price[j-1])
    else:
        if price[j-1] > price[j]:
            #무조건 팔아라
            w = w + (coin * price[j-1])
            coin = 0
w = w + (coin * price[n-1])
print(w)
