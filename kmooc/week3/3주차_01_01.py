kor = input("당신의 국어 성적은?")
kor = float(kor)

eng = input("당신의 영어 성적은?")
eng = float(eng)

math = input("당신의 수학 성적은?")
math = float(math)

avg = (kor + eng + math) / 3
print("3개 과목의 평균은",avg,"입니다.")
