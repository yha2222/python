def dan(a):
#for a in range(9, 2, -2):
    print("====={}단=====".format(a))
    for i in range(1, 9+1):
        if not i == 5 :
            print("{} * {} = {}".format(a, i, a*i))

dan(9)
dan(6)
dan(7)
dan(3)