num = int(input("구구단, 몇 단까지 입력 하실래요? : "))

for i in range(2, num+1, 1) :
    print("="*20)
    for j in range(2, 10, 1) :
        print(i, "*", j, " = ", i * j)
