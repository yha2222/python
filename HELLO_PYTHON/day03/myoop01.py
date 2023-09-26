class Animal:
    def __init__(self):
        self.age = 0
    
    def go1year(self):
        self.age += 1
        
class Human(Animal):
    def __init__(self):
        super().__init__() # 조상 호출
        self.nation = "korea"
    def immigrate(self, nation):
        self.nation = nation

if __name__ == '__main__':
    hum = Human()
    print(hum.nation)
    print(hum.age)
    hum.go1year()
    hum.immigrate("america")
    print(hum.nation)
    print(hum.age)