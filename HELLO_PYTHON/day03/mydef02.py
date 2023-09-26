def showDan(dan):
   # print(str(dan)+"*"+str(1)+"="+str(1*dan))
    
    for i in range(1, 9+1):
        print("{} * {} = {}".format(dan, i, dan * i))
        
showDan(7)