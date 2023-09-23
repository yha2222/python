# 랜덤함수를 이용하여 홀/짝을 출력
import random

rnd = random.random()
print(rnd)
if rnd > 0.5 :
    print("홀")
else :
    print("짝")


# from random import random
#
# rnd = random()
#
# if rnd > 0.5 :
#     print("짝")
# else :
#     print("홀")
