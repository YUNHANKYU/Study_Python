Input_Str = input("문자열 입력: ")
Input_find = input("찾아 바꿀 문자: ")
find_Length = len(Input_find)

index = Input_Str.find(Input_find)

if index == -1:
    print("바꿀 문자가 없습니다!")
else:
    beforeStr = Input_Str[0:index]
    changeStr = Input_Str[index:index+find_Length].upper()
    afterStr = Input_Str[index+find_Length:]
    result = beforeStr + changeStr + afterStr
    print(result)
