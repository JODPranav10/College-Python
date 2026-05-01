num = [12,7,3,1,2,4,5,6]
eve=[]
odd=[]
for i in num:
	if i % 2 == 0:
		eve.append(i)
	else:
		odd.append(i)
print("Display Original List:-",num)
print("Even Numbers:-",eve)
print("Odd Numbers:-",odd)
print("Even Numbers in the list:-", len(eve))
print("Odd Numbers in the list:-", len(odd))
print("Sum of Even Numbers:-",sum(eve))
print("Sum of Odd Numbers:-",sum(odd))
