def add():
    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))
    z = x + y
    print(f"The answer is {z}")

def sub():
    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))
    z = x - y
    print(f"The answer is {z}")

def muti():
    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))
    z = x * y
    print(f"The answer is {z}")

def div():
    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))
    if y == "0.0":
        print("Error: Cannot be divided by 0")
    else:
        z = x/y
        print(f"The answer is {z}")

def exp():
    x = float(input("Enter X: "))
    y= float(input("Enter Y: "))
    z = x ** y
    print(f"The answer is {z}")

def root():
    x = float(input("Enter X: "))
    y= float(input("Enter Y: "))
    z = x ** (1/y)
    print(f"The answer is {z}")

while True:
    print("---MENU---")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exponentiation")
    print("6.Roots")
    print("7.Quit")


    choice = input("Choose what you want to operate: ").strip()

    if choice == "1":
        add()
    elif choice == "2":
        sub()
    elif choice == "3":
        muti()
    elif choice == "4":
        div()
    elif choice == "5":
        exp()
    elif choice == "6":
        root()
    elif choice == "7":
        print("See ya!")
        break
    else:
        print("Please answer a vaild response\n") 

             #end