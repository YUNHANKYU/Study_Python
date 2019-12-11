input_str = input("문자열을 입력하세요: ")

l = len(input_str)

index = 0

while index < l:
    print("s[0:",index+1,"]=",input_str[0:index+1])
    index = index + 1
