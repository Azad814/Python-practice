class vehicle:
    def general_usage(self):
        print('use transportation')
class car(vehicle):
   # def __init__(self):
    print('i am car')
    #self.wheels=4
    #self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print('commute to work, vacation with family')

class motorcycle(vehicle):
    def __init__(self):
        print('i am motor cycle')
        self.wheels= 2
        self.has_roof= False 
    def specific_usage(self):
        self.general_usage()
        print('specific use; Road trip')
c= car()
m= motorcycle()
c.specific_usage()
print(issubclass(car, motorcycle))
