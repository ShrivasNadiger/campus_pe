def print_personal_bio_card(name,age,course,college,email):
  """
  this function prints the personal bio card 
  takes name,age,course,college and email as parameters and prints them in bio card
  """
  # construct the dict of data to print
  data={
    "Name":name,
    "Age":age,
    "Course":course,
    "College":college,
    "Email":email
  }

  #calculates the max_length by comapring all the key value pairs length
  max_length = max(len(f" {k} : {v} ") for k, v in data.items())
  width=max_length+5

# printing thr bio card and all the data using loop
  print("╔"+"="*(width-2)+"╗")
  print("║{:^{width}}║".format("STUDENT BIO CARD",width=width-2))
  print("╔"+"="*(width-2)+"╗")
  for key,values in data.items():
    print("║ {:<8}: {:<25} ║".format(key,values))
  print(f"╚{'='*(width-2)}╝")
def main():
  """
  takes input from user and pass it to the print_personal_bio_card()
  """
  name=input("Enter your name : ")
  age=input("Enter your Age : ")
  course=input("Enter your Course name : ")
  college=input("Enter your College name : ")
  email=input("Enter your Email  : ")
  print_personal_bio_card(name,age,course,college,email)

if __name__=="__main__":
  main()
