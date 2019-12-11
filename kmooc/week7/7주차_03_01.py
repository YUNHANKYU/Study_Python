msg = input("좋아하는 영어문장을 입력하세요 : ")
msgList = msg.split()
print("List: ", msgList)

Remove_Word = input("제거할 단어를 입력하세요 : ")
msgList.remove(Remove_Word)
print("제거 후 List: ", msgList)

Add_Word = input("추가할 단어를 입력하세요 : ")
msgList.append(Add_Word)
print("추가 후 List: ", msgList)
                 
delimiter = " "
Str = delimiter.join(msgList)
                 
print("join 후 문자열: ", Str)
