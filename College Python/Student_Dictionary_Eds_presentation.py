Student={
		" Name" : "Pranav",
		"PRN" : "040",
		}
print(Student,"\n") 											#Creating a dictionary
#output : {' Name': 'Pranav', 'PRN': '040'}
Student["Branch"]="ENTC" 										#Adding data
print(Student,"\n")
#output : {' Name': 'Pranav', 'PRN': '040', 'Branch': 'ENTC'}
Student["PRN"]="40"												#Mutability
print(Student,"\n")
#output : {' Name': 'Pranav', 'PRN': '40', 'Branch': 'ENTC'}
print(Student["Branch"])										#Accessing the data
remove_prn= Student.pop("PRN")									#Removal of data
print(Student)
print(Student.clear())											#Empty Dictionary