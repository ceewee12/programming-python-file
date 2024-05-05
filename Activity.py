class student:
    def setModule(self,m):
        self.__module__= m
    def getModule(self):
        return self.__module__
obj1 = student()
obj1.setModule("BIA101")
print(obj1.getModule())
obj2 = student()
obj2.setModule("BIA102")
print(obj2.getModule())

    
        