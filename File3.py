def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("Please select the operation:")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
Operation = input("Enter the operation:")
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
if Operation == "A":
    print(Num1, "+", Num2, "=", add(Num1,Num2))
elif Operation == "B":
    print(Num1, "-", Num2, "=", subtract(Num1,Num2))
elif Operation == "C":
    print(Num1, "*", Num2, "=", multiply(Num1,Num2))
elif Operation == "D":
    print(Num1, "/", Num2, "=", divide(Num1,Num2))
else:
    print("This is invalid input!")
