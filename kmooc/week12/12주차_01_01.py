inf = open('number.txt')
s = inf.readlines()
total = 0
mean = 0

for i in range(len(s)):
    total = total + int(s[i])

mean = total / len(s)
print('Number list = ', s, '\nTotal = ', total, '\nMean = ',round(mean,2))
