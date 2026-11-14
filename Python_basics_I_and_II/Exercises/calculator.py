num1=int(input("Enter 1st value:"))
num2=int(input("Enter 2nd value:"))
operator=input("Enter operator:")

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/": 
    print(num1/num2)
else:
    print("Invalid Operator!")