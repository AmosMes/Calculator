from art import logo
print(logo)

# Add function
def add(n1, n2):
  return n1 + n2

# Subtructing function
def sub(n1, n2):
  return n1 - n2

# Dividing function
def div(n1, n2):
  return n1 / n2

# Multiply function
def multi(n1, n2):
  return n1 * n2

# Power function
def power(n1, n2):
  return n1 ** n2

# Modulus function
def modulus(n1, n2):
  return n1 % n2

operations = {
  "+": add,
  "-": sub,
  "/": div,
  "*": multi,
  "**": power,
  "%": modulus
}
should_continue = True
while  should_continue:
# Printing the keys from the dictionary so the user will be able to pick a mathematical operation.
    num1 = float(input(f"What is the first number?: "))
    num2 = float(input(f"What is the second number?: "))

    for key, value in operations.items():
      print(key)
    operation_key = input(f"Pick an operation key from the line above: ")

# Calculation function based on the dictionary and the functions defined above, instead of the 7 lines of if statements below.
    calculation_function = operations[operation_key]
    answer = calculation_function(num1, num2)
# if operation_key == "+":
#   answer = add(num1, num2)
# elif operation_key == "-":
#   answer = sub(num1, num2)
# elif operation_key == "*":
#   answer = multi(num1, num2)
# else:
#   answer = div(num1, num2)
  
    print(f"{num1} {operation_key} {num2} = {answer}")

# The condition for the while loop , if yes the user will be able to do another calculation, if no the app will close.    
    calc_again = input(f"Would you like to calc again?: yes or no ")
    if calc_again == "no":
        should_continue = False
    else:
        should_continue = True
