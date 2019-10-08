Korean = int(input("국어성적: "))
English = int(input("영어성적: "))
Math = int(input("수학성적: "))
Mean = (Korean + English + Math) / 3

if Korean < 50 or English < 50 or Math < 50 :
    print("과락")
elif Mean >= 60 :
    print("합격")
else:
    print("불합격")
