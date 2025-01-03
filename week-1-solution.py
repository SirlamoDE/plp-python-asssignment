# Creating an application that that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15

def calculate(num1, num2, operator):
  """
  Performs a mathematical operation on two numbers.

  Args:
      num1 (float): The first number.
      num2 (float): The second number.
      operator (str): The mathematical operator (+, -, *, /).

  Returns:
      float: The result of the operation.
      None: If the operator is invalid or division by zero occurs.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero is not allowed.")
      return None
    else:
      return num1 / num2
  else:
    print("Invalid operator. Please enter +, -, *, or /.")
    return None

if __name__ == "__main__":
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Enter the operation (+, -, *, /): ")

  result = calculate(num1, num2, operator)

  if result is not None:
    print(f"{num1} {operator} {num2} = {result}")
