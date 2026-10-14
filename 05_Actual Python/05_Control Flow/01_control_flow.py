## IF and ELSE STATEMENTS

temperature = 25

if temperature >= 25:
    print("It's hot")

else:
    print("It's not hot")


## IF, ELIF AND ELSE LADER

temperature = int(input("Enter the number: "))

if temperature > 30:
    print("It's very hot")
elif temperature > 25:
    print("It's hot")
else:
    print("It's not hot")


## USING IF, ELIF & ELSE INSIDE IF AND ELSE OR ELIF

has_ticket = True
age = int(input("Enter your age: "))

if has_ticket:
    if age >= 18:
        print("Enjoy the show")
    else:
        print("Need supervision")
else:
    print("Buy a ticket")
