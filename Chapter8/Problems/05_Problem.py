def pattern(n):
    if(n==0):
        return
    print("*" *  n)
    pattern(n-1)
    
pattern(3) #prints firsts then 2 star next.    
# ***
# **
# *
