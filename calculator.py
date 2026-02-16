def calculator(num1,num2,operation):
   if operation == "+":
       return num1+num2
   elif operation == "-":
       return num1-num2
   elif operation == "*":
       return num1*num2
   elif operation == "/":
     if num2==0:
       return"Error cannot divide by zero"
     return num1/num2

   else:
       return"Invalid operation"

def area_trapezium(base1,base2,h):
    area=(base1+base2)*h/2
    return area
def is_prime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True


print("1.calculator")
print("2.Trapezium area")
print("3.prime number check")
choice = input("\nSelect a tool (1-3): ")
if choice=="1":
    num1=float(input("enter first number"))
    op=input("enter operation")
    num2=float(input("enter second number"))
    print(calculator(num1,num2,op))

elif choice=="2":
    base1=float(input("enter first base"))
    base2=float(input("enter second base"))
    h=float(input("enter h"))
    print((area_trapezium(base1,base2,h)))
elif choice=="3":
    num=int(input("enter number to check"))
    if is_prime(num):
        print(num,"is Prime!")
    else:
        print(num," is not Prime.")
else:
    print("Invalid operation")







