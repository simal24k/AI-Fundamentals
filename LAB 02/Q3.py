class Student:
    def __init__(self, attributemarks):
        self.__attributemarks = attributemarks

    def setmarks(self, marks):
        self.__attributemarks = marks
  
    def getmarks(self):
        return self.__attributemarks

    def calcgrade(self):
        gmarks = self.getmarks()   # FIX HERE
        if gmarks >= 50:
            return "PASS"
        else:
            return "FAIL"


s1 = Student(80)
s1.setmarks(70)
print(s1.calcgrade())

s2 = Student(30)
s2.setmarks(40)
print(s2.calcgrade())
