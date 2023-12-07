#program to find average marks of students

student_height=input("enter the marks").split()
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
    sum=0
for i in student_height:
    sum=int(sum)+int(i)
avg_height=sum/len(student_height)
print(f"total number of marks = {sum}")
print(f"number of student = {len(student_height)}")
print(f"average height = {avg_height}")

#program to find the heighest number 
# numbers=input("enter the numbers").split()
# for n in range(0,len(numbers)):
#     numbers[n]=int(numbers[n])
# high_score=0
# for i in range(0,numbers):
#     if i>numbers:
#         high_score=i
# print(f"highest number is {high_score}")

#program to add numbers within a range
starting_number=int(input("enter first number"))
ending_number=int(input("enter second number"))
total=0
for n in range(starting_number,ending_number):
    total+=n
print(f"sum of numbers{total}")
#prgram to find sum of even numbers
number=int(input("enter the maximum range"))
sum=0
for i in range(0,number+1,2):
    sum+=i
print(sum)