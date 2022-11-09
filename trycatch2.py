print("How many cats do you have?")
cats = input()

try:
    if (int(cats) >= 4):
        print("You have a lot of cats")
    else:
        print("That's not a lot of cats")
except ValueError:
    print("You did not enter a number!")
