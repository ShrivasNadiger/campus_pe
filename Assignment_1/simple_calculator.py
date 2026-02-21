def calculator(num_1:int,num_2:int)->None:
  """
  this function takes two interger parameter and prints the result 
  """
  print("*"*15 + "RESULT" + "*"*15)
  print(f" {num_1} + {num_2} = {num_1 + num_2}")
  print(f" {num_1} - {num_2} = {num_1 - num_2}")
  print(f" {num_1} * {num_2} = {num_1*num_2}")
  print(f" {num_1} / {num_2} = {num_1//num_2}")
  print(f" {num_1} % {num_2} = {num_1%num_2}")
  print(f" {num_1} ^ {num_2} = {num_1**num_2}")

#take input from the user and pass it to the calculator() function
a=input("Enter first number : ")
b=input("Enter second number (smaller than first number): ")
a,b=int(a),int(b)
calculator(a,b)

