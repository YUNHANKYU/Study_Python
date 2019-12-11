s = input("문자열을 입력하세요: ")

uppercaseCount = 0
lowercaseCount = 0
etcCount = 0

swapStr = s.swapcase()
print("대소문자 바꾼 결과: ", swapStr)

for i in swapStr:
    if i.isupper():
        uppercaseCount = uppercaseCount + 1
    elif i.islower():
        lowercaseCount = lowercaseCount + 1
    else:
        etcCount = etcCount + 1

print("대문자 개수는 ", uppercaseCount, "입니다.")
print("소문자 개수는 ", lowercaseCount, "입니다.")
print("대소문자가 아닌 문자의 개수는 ", etcCount, "입니다.")
