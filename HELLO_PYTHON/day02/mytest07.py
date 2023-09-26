# 1~100까지 수 중 랜덤값(com) 지정 50
# for문 10번 돌려서 10번 안에 맞추게 하기
# 숫자를 입력하시오 20
# 20 UP
# 숫자를 입력하시오 70
# 70 DOWN
# 숫자를 입력하시오 50
# (50) 정답입니다.
from random import random

com = int(random() * 100) + 1

res = True

for i in range(10):
    me = input("숫자를 입력하시오")
    ime = int(me)
    
    if ime == com :
        print("{} 정답입니다.".format(me))
        res = False
        break
    elif ime < com :
        print("{} UP".format(ime))
    else :
        print("{} DOWN".format(ime))
        
if not res :
    print("성공!")
else :
    print("10번 안에 맞추기 실패!")