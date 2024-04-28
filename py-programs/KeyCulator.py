# Welcome & Introduction
print("""Welcome To Key-Culator!
This program lets you do any simple calculations. The difference is ...
there is no buttons, so your keyboard will work hard!
That's why it's called Key-Culator.""")

KBs (Key Buttons): 
P for Plus 
M for Minus 
X for Times 
D for Over
R for Root
W for Power \n""")

# Program
opr = input("Enter a KB: ")

while opr != "Done":
    if opr == "P":
        number1 = int(input("Enter number 1: "))
        number2 = int(input("Enter number 2: "))
        print("The answer is", number1 + number2)

    elif opr == "M":
        number1 = int(input("Enter number 1: "))
        number2 = int(input("Enter number 2: "))
        print("The answer is", number1 - number2)

    elif opr == "X":
        number1 = int(input("Enter number 1: "))
        number2 = int(input("Enter number 2: "))
        print("The answer is", number1 * number2)

    elif opr == "D":
        number1 = int(input("Enter number 1: "))
        number2 = int(input("Enter number 2: "))
        print("The answer is", number1 / number2)

    elif opr == "R":
        number = int(input("Enter number: "))
        print("The answer is", number ** 0.5)

    elif opr == "W":
        number1 = int(input("Enter number 1: "))
        number2 = int(input("Enter number 2: "))
        print("The answer is", number1 ** number2)

    else:
        print("Invalid input.")

    opr = input("Enter a KB: ")

print("Thank you for using Key-Culator!")
