class Vehicle:
  def __init__(self, vehicleid, brand, rentpday):
    self.vehicleid = vehicleid
    self.brand = brand
    self.rentpday = rentpday
  def display(self):
    print(f"Vehicle ID:  {self.vehicleid}")
    print(f"Vehicle Brand:  {self.brand}")
    print(f"Rent per day:  {self.rentpday}")
  def calculaterent(self, days):
    return self.rentpday * days

V1 = Vehicle(110, "BYD", 2500)
V1.display()
V2 = Vehicle(92, "BMW", 1500)
V2.display()
print(f"Rent for 10 days:  {V2.calculaterent(10)}")
