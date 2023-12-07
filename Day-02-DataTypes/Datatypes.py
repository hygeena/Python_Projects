#program to find sum of two digits
# num=input("enter two digit number")
# sum=int(num[0])+int(num[1])
# print(sum)

#program to find the BMI
# weight=float(input("enter the weight"))
# height=float(input("enter the height"))
# height=height**2
# BMI=(weight/height)
# print(BMI) 

 #Program to find life in weeks left
 #appromixmate life expectancy - 90
# age=input("enter age")
# remaining_age=90-int(age)
# #no of weeks in an year is 52
# weeks_left=int(remaining_age)*52
# print(f"you have {weeks_left} weeks left in your life")

# Tip calculator
print("welcome to Tip calculator")
total_bill=input("what was the total bill?")
tip_percentage=input("what percentage tip would you like to give? 10,12 or 15?")
no_of_people=input("How many people to split the bill?")
payment_for_each_person=(float(total_bill)+(float(total_bill)*float(tip_percentage)/100))/float(no_of_people)
print(round(payment_for_each_person,2))
