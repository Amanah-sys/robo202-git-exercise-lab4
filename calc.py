def do(a,b,operation):
    if operation=="add":
        return a+b
    if operation=="subtract":
        return a-b
    if operation=="multiply":
        return a*b
    if operation=="divide":
        if b==0:
            print("Error: Division by zero") 
            return "Math Error"
    return a/b

print("CALCULATOR") 
print("Use add, subtract, multiply, divide") 
x=input("What is the first number?")
y=input("What is the second number?")
z=input("What operation would you like to perform?")

print ("Answer is:", do(int(x),int(y),z))

