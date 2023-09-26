def add_min_mul_div(a, b):
    return a+b, a-b, a*b, a/b

sum = add_min_mul_div(4, 2)

# tuple - 배열 말고 튜플 => 개수랑 똑같이 받든지 하나만 받음
print("sum", sum)   #sum (6, 2, 8, 2.0)
print("sum", sum[2]) #sum 8
#print("min", min)
#print("mul", mul)
#print("div", div)
