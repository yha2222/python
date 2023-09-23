# 1~100까지 수 중 랜덤값(com) 지정 50
# for문 10번 돌려서 10번 안에 맞추게 하기
# 숫자를 입력하시오 20
# 20 UP
# 숫자를 입력하시오 70
# 70 DOWN
# 숫자를 입력하시오 50
# (50) 정답입니다.
from random import random

rnd = random()
ran = int(rnd * 100) + 1

res = False

for i in range(10):
    me = input("숫자를 입력하시오")
    ans = int(me)
    
    if ans == ran :
        print("{} 정답입니다.".format(ran))
        res = True
        break
    elif ans < ran :
        print("{} UP".format(ans))
    else :
        print("{} DOWN".format(ans))
        
if res :
    print("끝")
else :
    print("10번 안에 맞추기 실패!")