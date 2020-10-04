# Has a relation of inheritance 
class engine:
    def __init__(self):
        self.cc = 1200
        self.Torque = 80
        print('Engine object created')

class car:
    def __init__(self):
        self.eng = engine()
        self.Brand = 'Maruthi'
        print('Car object created')

    def CarDetails(self):
        print(self.Brand)
        print(self.eng.cc)
        print(self.eng.Torque)


c = car()
c.CarDetails()