print("Add")
print("Sub")
print("Multiplication")
print("Subtraction")
print("Select option 1/2/3/4")



def add(x,y):
    print(f"The sum of {x} and {y} = {x+y}")

def subtract(x,y):
    print(f"The sub of {x} and {y}={x-y}")

def mul(x,y):
    print(f"The mul of {x} and {y}={x*y}")

def div(x,y):
    print(f"The div of {x} and {y}={x/y}")

def n(k):
    return
a=int(input("Write your option:"))

if a==1:
    x=int(input("Write the num"))
    y=int(input("Write the num"))
    add(x,y)

elif a==2:
    x=int(input("Write the num"))
    y=int(input("Write the num"))
    subtract(x,y)

elif a==3:
    x=int(input("Write the num"))
    y=int(input("Write the num"))
    mul(x,y)

elif a==4:
    x=int(input("Write the num"))
    y=int(input("Write the num"))
    div(x,y)

else:
    print(f"Invalid option the choice you entered {a} ")
    










    
