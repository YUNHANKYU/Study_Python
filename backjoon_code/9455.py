count = int(input())
arr = []

def boxMove():
    _sum =0
    box = []
    row, col = map(int, input().split())
    for i in range(row):
        box.append(list(map(int, input().split())))
    for j in range(col):
        oneCount = 0
        for k in range(row-1, -1, -1):
            #print("row-1 =", row-1, "k =", k)
            _sum = _sum + box[k][j] * ((row-1-k)-oneCount)
            if box[k][j] == 1:
                oneCount=oneCount+1
    return _sum
            
for i in range(count):
    arr.append(boxMove())
    print(arr[i])
