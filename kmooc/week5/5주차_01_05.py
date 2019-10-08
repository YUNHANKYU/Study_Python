name = '???'
count = 0


while name[0] != '김' and name[0] !='최' and name[0] != '이' and count < 5 :
    name = input("이름을 입력하세요 : ")
    count = count + 1


if count == 5 :
    print("5회 까지 입력 가능합니다")
else :
    print("성이 김, 최, 이 중에 있네요")
