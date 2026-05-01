marks=[15,14,17,18,20]
print(marks)
marks[2]=19
print(marks) 										#updated list [15,14,19,18,20]
marks.append(16)
#print(marks)										#updated list [15,14,19,18,20,16]
marks.insert(1,20)
#print(marks)										#updated list [15,20,14,19,18,20,16]
marks.remove(14)
#print(marks)										#updated list [15, 20, 19, 18, 20, 16]
marks.pop(0)
print("Detailed Marks:",marks)						#Detailed Marks: [20, 19, 18, 20, 16]