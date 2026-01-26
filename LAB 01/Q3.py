#Q3
numofstd = int(input("Enter number of students you want to store: "))
i =0
j =0
dict={}
while i<numofstd:
  i = i+1
  name = input("Enter student name: ")
  marks = int(input("Enter marks: "))
  dict[i] = (name, marks)

print("Student Records: ")
while j<numofstd:
  j=j+1
  print(dict[j][0],": ",dict[j][1])
