print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperooni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_chesse = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15;
elif size == "M":
    bill += 25
elif size == "L":
    bill += 30
else:
    print("Wrong chhoice ")

if pepperooni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_chesse == "Y":
    bill += 1

print(f"Your final bill is ${bill}")


