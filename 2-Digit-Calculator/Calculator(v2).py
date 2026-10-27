def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def muti(a,b):
    return a * b
def exp(a,b):
    return a ** b
def root(a,b):
    return a ** (1/b)
def div(a,b):
    if b == 0:
        print ("Error: Cannot be divided by 0")
    else:
        return a/b
while True:
    print("---Menu---\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    print("5. Exponentiation\n6. Roots\n7. Quit")

    choice = input("Choose what you want to operate: ")

    if choice == "7":
        print("See ya!")
        break
    elif choice in ["1","2","3","4","5","6"]:
        x = float(input("Enther the first number you want to operate: "))
        y = float(input("Enter the second number you want to operate: "))
    
        if choice == "1":
            print(f"The Answer is {add(x,y)}\n")
        elif choice == "2":
            print(f"The Answer is {sub(x,y)}\n")
        elif choice == "3":
            print(f"The Asnwer is {muti(x,y)}\n")
        elif choice == "4":
            print(f"The Answer is {div(x,y)}\n")
        elif choice == "5":
            print(f"The Answer is {exp(x,y)}\n")
        elif choice == "6":
            print(f"The Answer is {root(x,y)}\n")

        else:
            print("Please answer a vaild response\n")
#End