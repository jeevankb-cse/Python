#Q.Write a program to accept marks of 3 students and display them in a sorted manner.
marks=[]
f1=int(input("Enter marks here:"))
marks.append(f1)
f2=int(input("Enter marks here:"))
marks.append(f2)
f3=int(input("Enter marks here:"))
marks.append(f3)
marks.sort()

print(marks)
