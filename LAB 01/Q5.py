#Q5
num = int(input("Enter number of marks to be added: "))
i=0
marks={}
while i<num:
  marks[i] = int(input(f"Marks No.{i+1}: "))
  i=i+1

def calculate_avg(marks):
  j=0
  total=0
  avgmarks=0
  while j<num:
    total = total + marks[j]
    j=j+1

  avgmarks = total / num
  print("Average Marks: ", avgmarks)

calculate_avg(marks)
