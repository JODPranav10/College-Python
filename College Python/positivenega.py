num=int(input("Enter number:"))
def nop(num):
	if(num == 0):
		print("Zero")
	elif(num>0):
		print("Positive number:")
	else:
		print("Negative number:")
print(nop(num))