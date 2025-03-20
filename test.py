# import re
# phone_number = "87001112169"
# x = re.findall("^8.|^+7", phone_number)
# if x:
#     print("The phone number is correct")
# else:
#     print("The phone number is NOT correct")

# дата номер недели посчитать 52 недели в общем
import datetime
a = int(input("Enter the year: "))
b = int(input("Enter the month: "))
c = int(input("Enter the day: "))
x = datetime.datetime(a,b,c)

print(x.strftime("%W"))