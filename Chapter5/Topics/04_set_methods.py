s={1,2,3,4,5,6,4,8,9,"Jeevan"}
#print(s,type(s))#{False, 1, 2, 3, 4, 5, 6, 8, 9, 'Jeevan'}<class 'set'>
#s={1,2,3,4,5,6,4,8,9,"Jeevan",True}#is treated as 1
#print(s,type(s))#{1, 2, 3, 4, 5, 6, 8, 9, 'Jeevan'} 
s.add(99)#{1, 2, 3, 4, 5, 6, 99, 8, 9, 'Jeevan'} <class 'set'>
print(s,type(s))
nums = [x for x in s if isinstance(x, int)]
print(sorted(nums))#[1, 2, 3, 4, 5, 6, 8, 9, 99]
