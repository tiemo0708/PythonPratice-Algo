class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__() #super로 다중상속 불가능
        Unit.__init__(self)
        Flyable.__init__(self)
#드랍쉽
dropship = FlyableUnit()