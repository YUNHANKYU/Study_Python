n = int(input())
tile = []

tile.append(0)
tile.append(1)
tile.append(2)

for i in range(3, n+1):
    tile.append((tile[i-1] + tile[i-2]) % 15746)

print(tile[n] % 15746)
