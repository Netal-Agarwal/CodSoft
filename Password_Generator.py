import random

def generate_password(length, complexity):
  """
  This function helps to generate the password with two arguments as length and complexity.
  """
  lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
  uppercase_letters = lowercase_letters.upper()
  digits = "0123456789"
  symbols = "!@#$%^&*()"

  if complexity == "low":
    char_set = lowercase_letters + digits
  elif complexity == "medium":
    char_set = lowercase_letters + uppercase_letters + digits
  elif complexity == "high":
    char_set = lowercase_letters + uppercase_letters + digits + symbols
  else:
    raise ValueError("Complexity can only be low,medium or high.")

  password = "".join(random.sample(char_set, length))
  return password

def get_user_input():
  """
  Allows the user to enter length and complexity level of the password as mentioned earlier.
  """
  while True:
    try:
      length = int(input("Enter the length of the password (minimum 8 characters): "))
      if length < 8:
        print("Length of the password has to be at least 8 characters.")
        continue
      complexity = input("Enter password complexity (low, medium, or high): ").lower()
      return length, complexity
    except ValueError:
      print("Invalid input.")

def main():
  length, complexity = get_user_input()
  password = generate_password(length, complexity)
  print("Your generated password is:", password)

if __name__ == "__main__":
  main()
  
  
