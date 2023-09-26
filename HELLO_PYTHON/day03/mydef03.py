from random import random
def getHJ():
    ret = "홀"
    if random() > 0.5 :
        ret ="짝"
    return ret
        
com = getHJ()
print("com", com)