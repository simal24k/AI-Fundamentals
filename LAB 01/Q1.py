#Q1
name = input("Enter name: ")
marks = float(input("Enter marks: "))
print("\nstudent name:", name)
print("marks:", marks)
if marks >= 85 and marks < 101 :
   print("Grade A")
elif marks >= 70 and marks < 85:
   print("Grade B")
elif marks >= 50 and marks < 70:
   print("Grade C")
elif marks < 50 and marks >= 0:
   print("FAIL")
else:
   print("incorrect entry - please try again ")
