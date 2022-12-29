class Car:
    def __init__(self):
        self.color="검정"
        self.size=16
        self.model="ww"
        
    def forward(self):
        print("{0}가 전진합니다.".format(self.model))
        
        def backword(self):
            pass
    def turn_right(self):
        print("{0}가 우회전합니다.".format(self.model))
        
    def turn_left(self):
        print("{0}가 좌회전합니다.".format(self.model))
        
    
if __name__=="__main__":
    car = Car()
    car.turn_left()