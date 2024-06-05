def addition(a,b):
    sum=a+b
    print("The sum of the numbers is: ",sum)

def subtraction(a,b):
    diff=a-b
    print("The differnece of the numbers is: ",diff)

def multiplication(a,b):
    mul=a*b
    print("The product of the numbers is: ",mul)

def division(a,b):
    divide=a/b
    print("The quotient of the numbers is: ",divide)

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

while True:
    print("**********************")
    print("1. Add.")
    print("2. Subtract.")
    print("3. Multiply.")
    print("4. Divide.")
    print("5. Exit.")
    print("**********************")
    
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        addition(num1,num2)
        
    elif choice==2:
        subtraction(num1,num2)
        
    elif choice==3:
        multiplication(num1,num2)
        
    elif choice==4:
        division(num1,num2)
        
    elif choice==5:
        exit()
        
    else:
        print("Invalid input..")

