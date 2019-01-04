def printYellow():
    print("You like Yellow Color")


def printGreen():
    print("You like Green Color")

def printBlack():
    print("You like Black Color")

def printWhite():
    print("You like White Color")

ColorSelect = {
    0 : printYellow,
    1 : printGreen,
    2 : printBlack,
    3 : printWhite
}



user_input = int(input('enter the color you want to print on the console :'))

if user_input >= 0 and user_input <=3:
    ColorSelect[user_input]()
