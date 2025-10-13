#NORAML PROGRAM:
f=int(input("Enter temperature in F:"))
c=5*(f-32)/9
print(c)

#BY APPLYING THE FUNCTION TO CONVERT °C TO F:
def f_to_c(f):
    return 5*(f-32)/9
f=int(input("Enter temperature in F:"))
print(f"{f_to_c(f)} °C")
#Decimal points with 2 numbers
def f_to_c(f):
    return 5*(f-32)/9
f=int(input("Enter temperature in F:"))
c=f_to_c(f)
print(f"{round(c,2)}°C")




