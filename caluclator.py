#varialbes
x = input("Enter your first number: ") # asking for input
y = input("Enter your second number: ")# asking for input
add = '+' # operator
sub = '-' # operator
mul = '*' # operator
div = '/' # operator
sign = input("What operator") # the operator type


if sign == add:
    print(float(x) + float(y)) # if the operator equals add, add them together
elif sign == sub:
    print(float(x) - float(y)) # if the operator equals sub, subtract them together
elif sign == mul:
    print(float(x) * float(y))  # if the operator equals mul, multiply them together
elif sign == div:
    print(float(x) / float(y))  # if the operator equals div, divide them together
else:
   print("No Valid operator") # if there is no 'Valid' operator available then print this         
   



   
