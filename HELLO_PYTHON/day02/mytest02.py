# 첫 수를 입력하시오 1
# 끝 수를 입력하시오 5
# 1에서 5까지의 합은 15입니다.

a = input("첫 수를 입력하시오")
b = input("끝 수를 입력하시오")
sum = 0

arr = range(int(a), int(b)+1)

for i in arr:
   sum += i 

print("{}에서 {}까지의 합은 {}입니다.".format(a, b, sum))