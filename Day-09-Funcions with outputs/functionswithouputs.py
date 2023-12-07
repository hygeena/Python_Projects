#program to convert firstname and lastname into title case
def convert(fname,lname):
    fullname=fname.title()+" "+lname.title()
    return f"{fullname}"
fname=input("enter firstname")
lname=input("enter last name")
fullname=convert(fname,lname)
print(fullname)

#calculator function
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def product(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
