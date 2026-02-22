def string_manipulator(value:str):
  """
  This Prints all the String manipulation of a string
  """
  print("Original : ",value)
  print(f"Charecteristics (with spaces) : {len(value)}")
  stripped_value="".join(value.split())
  print(f"Charecteristics (without spaces) : {len(stripped_value)}")
  words=value.split(" ")
  print(f" Words : {len(words)}")
  upper_case=value.upper()
  print(f"Upper Case : {upper_case}") #prints Upper CAse
  lower_case=value.lower()
  print(f"Lower Case : {lower_case}") #prints lower CAse
  Title_case=value.title()
  print(f"Title Case : {Title_case}") #Printys Title case
  first_word=words[0]
  print(f"First Word : {first_word}") #prints fiorst word
  last_word=words[-1]
  print(f"Last word : {last_word}")#prints last word
  
  print(f"Reversed : {value[::-1]}")#reverses string

def main():
  value=input("Enter the Sentence : ")
  string_manipulator(value=value)

if __name__ == "__main__":
  main()