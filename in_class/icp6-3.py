# Iris Canavan, Section 3

def main():
    print("Welcome to my calculator ")
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    strOperation = input("What do you want to calculate? (area (a), circumference (c)): ")
    fOperations(strOperation, length, width)

def fOperations(pOperation, pLength, pWidth):
    if pOperation == "a":
        Result = fCalcArea(pLength, pWidth)
        print("The Area of the rectangle = ", Result)
    elif pOperation == "c":
        Result= fCalcCircumference(pLength, pWidth)
        print("The circumference of the rectangle = ", Result)

def fCalcArea(pLength, pWidth):
    Result = pLength * pWidth
    return Result

def fCalcCircumference(pLength, pWidth):
    Result = 2 * (pWidth + pLength)
    return Result

main()
