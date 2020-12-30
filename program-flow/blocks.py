age = int(input("What is your age?"))

if age < 18:
    print(f"Please come back in {18 - age} years")
elif age >= 900:
    print("Sorry, yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Put a X in the box")
