def decimal_points():
    try:
        decimal_points_1 = float(input("\nHow many decimal places : "))
    except ValueError:
        print("\nPlease enter a number, if float is entered, it will be rounded")
        decimal_points()
    return decimal_points_1

decimal_points_1 = decimal_points()
decimal_points_2 = round(decimal_points_1)

if decimal_points_2>decimal_points_1:
    print("\nThe number of decimal point in the solution was rounded up to {}".format(decimal_points_2))
elif decimal_points_2<decimal_points_1:
    print("\nThe number of decimal point in the solution was rounded down to {}".format(decimal_points_2))
else:
    print("\nThe solution will have {} decimal points".format(decimal_points_2))

operations = ["+", "-", "*", "/"]
op = input("\nPlease enter operation, +, -, /, *: ")

while op not in operations :
    op = input("\nInvalid Operator, try again, +, -, /, *: ")


def num_input():    
    try:
        num1 = float(input("\nEnter the 1st number: "))
        num2 = float(input("\nEnter the 2nd number: "))

    except ValueError:
            print("\nNon-Numeric input, try again")
            num_input()
    return num1,num2

num1,num2 = num_input() 
  
def calc():
        if op == "+":
            return num1+num2

        elif op == "-":
            return num1-num2

        elif op == "/":
            return num1/num2

        else:
            return num1*num2
ans = calc()

print("\nThe answer is to {} {} {} is : {:.{}f}\n".format(num1,op,num2,ans,decimal_points_2))