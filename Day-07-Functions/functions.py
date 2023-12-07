def greet():
    print("hello")
    print("how are you")
    print("i am fine")

def calc():
    for i in range(10,0,-1):
        print(i)
calc()
greet()
#functions with parameteres
def greet_with(name,location):
    print(f"hello {name}")
    print(f"your location is {location}")
greet_with("albert","canada")

#postional arguments arguments passing to the fucntions based on the positions
def posi_arg(a,b,c):
    d=int(a+b+c)
    print(f"sum is {d}")
posi_arg(1,2,3)
def kw_arg(a,b,c):
    d=a+b-c
    print(d)
kw_arg(c=2,a=3,b=2)

