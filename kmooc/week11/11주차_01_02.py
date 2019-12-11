import random

namelist= []
oxlist= []

count = int(input("인원을 입력하세요: "))

for i in range (count):
    name = input("이름을 입력하세요: ")
    namelist.append(name)

for i in range (count) :
    oxlist.append(random.choice(['o', 'x']))

tname = tuple(namelist)
print(tname)

t = list(zip(tname, oxlist))
print(t)
