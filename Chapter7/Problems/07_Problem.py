#Write the program to print the follwing star pattern.
#   *
#  ***
# ***** for n=3 ?

'''
For n=3
  *
 ***
*****

'''
n=int(input("Enter the number:"))
for i in range(1,n+1): #n=3
    print(" "*(n-i),end="") #n-1=2,n-2=1,n-3=0;("Spaces"),So this controls alignment.
    print("*"*(2*i-1),end="") #(2*i-1)=Formula,i=1,2,3....n.
    print("")