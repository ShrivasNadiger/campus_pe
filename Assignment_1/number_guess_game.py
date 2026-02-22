import random
best_score=None
while True:
  secret_number=random.randint(1,100)
  print("Let's Start...")
  attempts=7
  used_attempts=0
  print("You Have 7 attempts to Guess The Number!! All the Best buddy..!!")

  while used_attempts<attempts:
    try:
      predicted_number=int(input("Enter the Number (1-100): "))
      used_attempts+=1

      if predicted_number==secret_number:
        print("Congragulations!! you Guessed it Right..")

        if best_score is None or used_attempts<best_score:
          print(f"NEW BEST SCORE : {used_attempts}")
        else:
          print(f"Your Best Score is {best_score} Try to beat it..")
        break
      
      elif abs(predicted_number-secret_number)<=5:
        print("You are very near..")

      elif predicted_number>secret_number:
        print("Too High")

      else:
        print("Too Low")
      
      print(f"Attempts left : {attempts-used_attempts}")
    except ValueError:
      print("Invalid Input..please enter a valid number")
  else:
    print("Failed.. the Secret Number was : ",secret_number)
  try_again=input("Do you want to try again (y/n) : ").lower()
  if try_again !='y':
    break