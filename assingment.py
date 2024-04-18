# calculator

playing = True

while playing:
  first_number = int(input("Choose a number:\n"))
  second_number = int(input("Choose another one:\n"))

#string 내에서 탭 하는 거 알고 싶어. 
  operation = input("Choose an operation:\n    Options are: +, -, * or /.\n    Write 'exit' to finish.\n")
  if operation == "+":
    print("Result:", first_number + second_number)
  elif operation == "-":
    print("Result:",first_number - second_number)
  elif operation == "*":
    print("Result:",first_number * second_number)
  elif operation == "/":
    print("Result:",first_number / second_number)
  elif operation == "exit":
    playing = False
    print("See you :)")
