#9.Write a program to print the following star pattern:
***
* *
***?


Answer=>
'''
* * *
*   *  for n=3 
* * *
'''
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if(i==1 or i==n):
       print("*"*n,end="")#n=3,First and Last row it prints.
    else:                  #Second line printing statement
        print("*",end="")#Prints * (first star).
        print(" "*(n-2),end="")#Prints (n-2) spaces → 3-2=1 space.
        print("*",end="")#Prints * (last star).
    print("")   #Output:   ***
                #          * *
                #          ***

  
