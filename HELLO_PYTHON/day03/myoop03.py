class Vehicle:
    # 생성자
    def __init__(self):
        print("constructor")
        self.cnt_wheel = 4
        
    def trans(self, wheel):
        self.cnt_wheel = wheel
    # 소멸자   
    def __del__(self):
        print("destroyer")
        
    def __str__(self):
        return "cnt_wheel:{}".format(self.cnt_wheel)

if __name__ == '__main__':
    veh = Vehicle()
    print(veh)
    veh.trans(2)
    print(veh)