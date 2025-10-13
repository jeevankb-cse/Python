def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
        

l=["jeevan","sanjay","pradeep","an"]
print(rem(l,"an"))

