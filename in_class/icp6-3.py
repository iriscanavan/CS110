# Iris Canavan, Section 3

def main():
    print("Welcome to my calculator ")
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    str_operation = input("What do you want to calculate? (area (a), circumference (c)): ")
    operations(str_operation, length, width)

def operations(pOperation, pLength, pWidth):
    if pOperation == "a":
        result = calc_area(pLength, pWidth)
        print("The Area of the rectangle = ", result)
    elif pOperation == "c":
        result= calc_circumference(pLength, pWidth)
        print("The circumference of the rectangle = ", result)

def calc_area(pLength, pWidth):
    result = pLength * pWidth
    return result

def calc_circumference(pLength, pWidth):
    result = 2 * (pWidth + pLength)
    return result

main()
