
#random number generation
import random
number=random.randint(1,10)
print(number)
random_float=random.random()*5
print(random_float)

#Lists
names=["Angela","Jhon","Roy","David"]
names_len=len(names)
name_select=random.randint(0,names_len-1)
print(f"{names[name_select]} is going to pay the bill today")

#Nested list
even_numbers=[2,4,6,8,10]
odd_numbers=[1,3,5,7,9]
numbers=[even_numbers,odd_numbers]
print(numbers)
print(numbers[0][0]) #output is 2

#How to create a random decimal number from 0 to 5
rand_float=random.random()*5
print(rand_float)