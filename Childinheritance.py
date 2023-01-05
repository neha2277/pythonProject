from Oopsdemo import Calculator


class ChildImp(Calculator): 

    num2= 200

    def __init__(self):
            Calculator.__init__(self,19,26)

    def getCompleteData(self):
            return self.num2 + self.num + self.Addition()



obj2 = ChildImp()
print(obj2.getCompleteData())

