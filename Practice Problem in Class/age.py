from datetime import datetime as dt
b_year=int(input("Enter Your Birth year: "))
c_year=dt.now().year
result=c_year - b_year
print("Age:-",result)