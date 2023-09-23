# 홀/짝을 선택하시오 홀
# 나: 홀
# 컴: 짝
# 결과: 짐
import random

com =''
res =''
a = input("홀/짝을 선택하시오")
print("나: " + a)

rnd = random.random()
if rnd > 0.5 : 
    com = '홀' 
else :
    com = '짝'
print("컴: " + com)
    
# 자바만 equals
if com == a:
    res = '이김'
else :
    res = '이김'
print("결과: " + res)