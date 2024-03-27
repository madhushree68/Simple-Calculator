import math
print("----CALCULATOR------")
def sum(a,b):
    a+=b
    return a
def sub(a,b):
    if (a>b):
        a-=b
        return a
    else:
        b-=a
        return b
def mul(a,b):
    a*=b
    return a
def div(a,b):
    q=a/b
    r=a%b
    print("quotient is",q)
    print("remainder is",r)
def sqrt(a):
    x=math.sqrt(a)
    return x
while(True):
    print("\n\nChoose the operation you want to perform")
    print("\n1.Addition\t2.Subtraction\t3.Multiplication\t4.Division\t5.Squareroot\t6.Exit\n")
    choice=int(input("Enter the choice"))
    if choice==1:
        print("enter two numbers")
        num1=int(input('>'))
        num2=int(input('>'))
        print("The sum is",sum(num1,num2))
    elif choice==2:
         print("enter two numbers")
         num1=int(input('>'))
         num2=int(input('>'))
         print("The subtraction is",sub(num1,num2))
    elif choice==3:
         print("enter two numbers")
         num1=int(input('>'))
         num2=int(input('>'))
         print("The multiplication is",mul(num1,num2))
    elif choice==4:
         print("enter two numbers")
         num1=int(input('>'))
         num2=int(input('>'))
         print("The division is",div(num1,num2))
    elif choice==5:
         print("enter the number")
         num1=int(input('>'))
         print("The squarerrot is",sqrt(num1))
    else:
        print("Exit")

    
        


