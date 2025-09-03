friends=["Apples","Orange",5,"Akash",56.1245,False]
print(friends)
friends.append("Sandwtich")
print(friends)
l1=[1,2,3,4,5,6,7,55,9]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(4,3333)#Insert 3333 such that its index in the list is 3
print(l1)
l1.sort()
print(l1)
print(l1.pop(4))
print(l1)
value=l1.pop(4)
print(value)
print(l1)
l1.remove(4)
print(l1)
l1 = [1, 2, 3, 4, 7, 9, 55, 3333]

# Remove all numbers between 1 and 9 (inclusive)
l1 = [x for x in l1 if not (1 <= x <= 9)]

print(l1)

