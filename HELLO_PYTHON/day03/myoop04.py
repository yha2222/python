# 만수르, 푸틴, 트럼프 클래스 만들고 네가지 찍기
class Mansuru:
    def __init__(self):
        self.money = 2400
        self.cnt_building = 10;
    def buyBuilding(self, money):
        self.cnt_building += money
        self.money -= money
        print("{0}채 빌딩을 구입하는 데 {1}조원 사용".format(self.cnt_building, money))

class Putin:
    def __init__(self):
        self.cnt_nuclear = 10000
    def war(self):
        self.cnt_nuclear -= 1
        print("전쟁에 사용 후 남은 핵 개수는 {}개".format(self.cnt_nuclear))

class Trump:
    def __init__(self):
        self.cnt_employee = 2000;
    def youFire(self):
        self.cnt_employee -= 10

class YoungNam(Mansuru, Putin, Trump):
    def __init__(self):
        Mansuru.__init__(self)
        Putin.__init__(self)
        Trump.__init__(self)
    
if __name__ == '__main__':
    son = YoungNam()
    print(son.money)
    print(son.cnt_nuclear)
    print(son.cnt_employee)
    son.buyBuilding(500)
    for i in range(10):
        son.war()
    son.youFire()
    print(son.money)
    print(son.cnt_nuclear)
    print(son.cnt_employee)
    