birthdate = {}

def add_birth(num):
    for i in range(num):
        input_name = input("이름: ")
        input_birth = int(input("생일: "))
        birthdate[input_name] = input_birth

add_birth(5)
print(birthdate)


name=input("생일을 삭제하고 싶은 사람의 이름을 입력하세요: ")
birthdate.pop(name)

print(name in birthdate)
print(birthdate)
