class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self) -> None:
        
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # 먼저 상속 받은 class의 생성자만 실행됨
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit() 