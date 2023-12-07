#Program for Leap Year
year=int(input("enter the year"))
if year % 4==0:
    if year% 100==0:
        if year%400 ==0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
        

#pizza price calculator
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N") # Do you want extra cheese? Y or N
if size == "S":
  price= 15
  if add_pepperoni=="Y":
    price=int(price)+2
elif size=="M":
  price=20
  if add_pepperoni =="Y":
    price=int(price)+3
elif size=="L":
  price=25
  if add_pepperoni=="Y":
    price=int(price)+3
if extra_cheese=="Y":
  price=int(price)+1
print(f"Your final bill is: ${price}.")

                                            #Love calculator
                                        # To work out the love score between two people:
                                        # Take both people's names and check for the number of times the letters in the word TRUE occurs.

                                        # Then check for the number of times the letters in the word LOVE occurs.

                                        # Then combine these numbers to make a 2 digit number.

                                        # For Love Scores less than 10 or greater than 90, the message should be:

                                        # "Your score is *x*, you go together like coke and mentos."
                                        # For Love Scores between 40 and 50, the message should be:

                                        # "Your score is *y*, you are alright together."
                                        # Otherwise, the message will just be their score. e.g.:

                                        # "Your score is *z*."
print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?") 
name=name1+name2
name_together=name.lower()
t=name_together.count("t")
r=name_together.count("r")
u=name_together.count("u")
e=name_together.count("e")
true=t+r+u+e
l=name_together.count("l")
o=name_together.count("o")
v=name_together.count("v")
e=name_together.count("e")
love=l+o+v+e
lovecalc=str(true)+str(love)
if int(lovecalc) <10 or int(lovecalc) > 90:
  print(f"Your score is {lovecalc}, you go together like coke and mentos.")
elif int(lovecalc) >=40 and int(lovecalc) <=50:
  print(f"Your score is {lovecalc}, you are alright together.")
else:
  print(f"Your score is {lovecalc}.")