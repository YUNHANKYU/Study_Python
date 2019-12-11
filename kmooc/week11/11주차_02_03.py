info = {'이름':'윤한규', '나이': 24, '주소': '포항시 북구 양덕동', '전공': '컴퓨터공학'}
print(info['이름'], "님에 대한 다음의 정보가 저장되어 있습니다. ")
print(info.keys())
key = input("알고 싶은 정보를 입력하세요: ")
print(info.get(key))
