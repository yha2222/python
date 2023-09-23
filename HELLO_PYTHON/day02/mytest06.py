# 첫 수를 입력하시오 1
# 끝 수를 입력하시오 10
# 배수를 입력하시오 5
# 1에서 10까지 5의 배수의 합은 15입니다.

start = input("첫 수를 입력하시오")
end = input("끝 수를 입력하시오")
dbl = input("배수를 입력하시오")
sum = 0;

str = int(start)
ed = int(end)
db = int(dbl)

arr = range(str, ed+1)

for i in arr :
    if i%db == 0 :
        sum += i

print("{}에서 {}까지 {}의 배수의 합은 {}입니다.".format(start, end, dbl, sum))