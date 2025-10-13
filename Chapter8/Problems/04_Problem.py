def sum(n): #Function definition ,sum(4)
    if(n==1): #Base case
        return 1
    return sum(n-1) + n #Recursive step,= sum(3) + 4,= (sum(2) + 3) + 4,= ((sum(1) + 2) + 3) + 4
print(sum(4))

#output:10            #sum(2) = 1 + 2 = 3
                      # sum(3) = 3 + 3 = 6
                      # sum(4) = 6 + 4 = 10