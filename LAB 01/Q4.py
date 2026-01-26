#Q4
choice = 0
while choice != 3:
   print("\n1. Add TWO numbers\n2. Subtract TWO numbers\n3. Exit")
   choice = int(input("Enter choice: "))
   if choice == 3:
    print("Exiting program...")
   else:
    fnum= int(input("Enter first number: "))
    snum= int(input("Enter second number: "))
    if choice == 1:
     result = fnum +snum
     print("Result: ", result)
    else:
     if fnum>snum:
      result = fnum - snum
      print("Result: ", result)
     else:
      result = snum-fnum
      print("Result: ", result)


