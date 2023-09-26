# 가위/바위/보를 입력하시오 가위
# 나: 가위
# 컴: 보 0.66 0.33
# 결과: 이김
from random import random

com = ""
me = input("가위/바위/보를 입력하시오")
res = ""

rnd = random()

if rnd > 0.66 :
    com = "가위"
elif rnd > 0.33 :
    com = "바위"
else :
    com = "보"

if com == "가위" and me == "가위": result = "비김"
if com == "가위" and me == "바위": result = "이김"
if com == "가위" and me == "보": result = "짐"

if com == "바위" and me == "가위": result = "짐"
if com == "바위" and me == "바위": result = "비김"
if com == "바위" and me == "보": result = "이김"

if com == "보" and me == "가위": result = "이김"
if com == "보" and me == "바위": result = "짐"
if com == "보" and me == "보": result = "비김"

print("나: " + me)
print("컴: {}".format(com))
print("결과: ", result)

#
# if com == me :
#     print("비겼습니다")
# elif com == "바위" and me == "가위" :
#     print("졌습니다")
# elif com == "가위" and me == "보" :
#     print("졌습니다")
# elif com == "보" and me == "바위" :
#     print("졌습니다")
# else :
#     print("이겼습니다")
