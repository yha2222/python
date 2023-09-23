# 첫 수를 입력하시오 7
# 두번째 수를 입력하시오 8
# 7은 8보다 작다
# 9는 8보다 크다
# 6은 6과 같다

a = input("첫 수를 입력하시오")
b = input("두번째 수를 입력하시오")

aa = int(a)
bb = int(b) 

if aa > bb :
    print("{}는 {}보다 크다".format(a, b))
elif aa < bb :
    print("{}는 {}보다 작다".format(a, b))
else :
    print("{}와 {}는 같다".format(a, b))