N = int(input())
dungChi = [list(map(int, input().split())) for i in range(N)]
rank = [1] * N

for i in range(len(dungChi)):
    for j in range(len(dungChi)):
        if dungChi[i][0] < dungChi[j][0] and dungChi[i][1] < dungChi[j][1]:
            rank[i] += 1
            
print(*rank)

