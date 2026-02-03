class Employee:
  def __init__(self, empid, ename):
     self.empid = empid
     self.ename = ename

class Fulltimeemployee(Employee):
  def __init__(self, empid, ename, msalary):
    super().__init__(empid, ename)
    self.msalary = msalary

  def calcsalary(self):
    return self.msalary


class Parttime(Employee):
  def __init__(self, empid, ename, hworked, hrate):
    super().__init__(empid, ename)
    self.hworked = hworked
    self.hrate = hrate

  def calcsalary(self):
    return self.hworked * self.hrate

e1= Fulltimeemployee(688,"Simal",10000)
e1.calcsalary()
print(f"Employee Name: {e1.ename}")
print(f"Salary: {e1.calcsalary()}")
e2 = Parttime(2005, "Hassan",160,100)
e2.calcsalary()
print(f"Employee Name: {e2.ename}")
print(f"Salary: {e2.calcsalary()}")
