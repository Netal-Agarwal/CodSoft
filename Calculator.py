def ask_for_number(num):
  """
  Keeps asking the user for a value until they enter a real number. 
  """
  while True:
    try:
      number = float(input("Enter the number in float"))
      return number
    except ValueError:
      print(" That doesn't look like a number.Please try again!")

def pick_operation():
  """
  Keeps asking the user for a symbol until they choose a valid math operation. 
  """
  while True:
    operator = input("Pick an operation (+, -, *, /, %, ^, pow): ")
    if operator in ["+", "-", "*", "/", "%", "^", "pow"]:
      return operator
    else:
      print("That's not a real math symbol.Please try again!")

def calculate(first_number, second_number, operation):
  if operation == "+":
    return first_number + second_number
  elif operation == "-":
    return first_number - second_number
  elif operation == "*":
    return first_number * second_number
  elif operation == "/":
    if second_number == 0:
      print(" We can't divide by zero. Try again!")
      return None
    else:
      return first_number / second_number
  elif operation == "%":
    if second_number == 0:
      print("We can't divide by zero to get a remainder. Try again!")
      return None
    else:
      return first_number % second_number
  elif operation == "^" or operation == "pow":
    return first_number ** second_number
  else:
    return None

def lets_calculate():
  """
  Ask the user to enter numbers, pick an operation, 
  and displays the answer. 
  """
  # Get numbers from the user
  first_number = ask_for_number("Give me the first number: ")
  second_number = ask_for_number("Give me the second number: ")

  # Get operator from the user
  operation = pick_operation()

  # Perform calculation and display result
  result = calculate(first_number, second_number, operation)
  if result is not None:
    print(f"{first_number} {operation} {second_number} = {result}")

if __name__ == "__main__":
  lets_calculate()
  
  
  
  
  
  
  
