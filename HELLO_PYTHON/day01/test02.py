# 좋아하는 수를 넣으세요 5
# 좋아하는 수를 또 넣으세요 6
# 5와 6의 합은 11입니다.

a = input("좋아하는 수를 넣으세요")
b = input("좋아하는 수를 또 넣으세요")
sum = int(a) + int(b)

print(a + "과 "+ b + "의 합은 " + str(sum) + "입니다.")
print("{}와 {}의 합은 {}입니다.".format(a, b, sum))
# console.log 개념
print(a, "와 ", b, "의 합은 ", sum, "입니다.")