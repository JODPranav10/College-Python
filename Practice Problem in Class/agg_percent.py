import math
def cal(marks, total_courses):
	if any(mark < 40 for mark in marks):
		return "FAIL"
	total_marks=sum(marks)
	agg_percent=(total_marks/(total_courses))
	if agg_percent > 75:
		grade= "Distinction"
	elif agg_percent >= 60:
		grade= "A"
	elif agg_percent >= 50:
		grade= "B"
	elif agg_percent >= 40:
		grade = "C"
	else :
		grade = "FAIL"
	return (agg_percent, grade)
num_courses = int(input("Enter number of num_courses: "))
marks = list(map(int, input("Enter marks separated by space: ").split()))
result = cal(marks, num_courses)
if result == "FAIL":
	print("FAIL")
else:
	agg_percent, grade = result
	print(f"Aggregate Percent: {agg_percent:.2f}")
	print(f"Grade: {grade}")
