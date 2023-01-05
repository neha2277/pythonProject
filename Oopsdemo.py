#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __inti__
#new keyword is not required when you create object

class Calculator:
    num = 100

    def __init__(self,a,b):
        self.firsnumber = a
        self.secondnumber = b

    def getData(self):
        print("i m learning the new language")

    def Addition(self):
        return self.firsnumber + self.secondnumber + self.num


obj = Calculator(2,4) # initalizing the object
obj.getData()  # To call a self method
print(obj.Addition())
print(obj.num)
