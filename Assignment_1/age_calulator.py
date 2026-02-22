#import datetime library for getting the current years
from datetime import datetime
#we can handle the invalid input trough try and except block
try:
    birth_year = int(input("Enter your birth year: "))
    current_year = datetime.now().year
    
    age = current_year - birth_year
    
    print("Age:", age)
    print("Age in months:", age * 12)
    print("Age in days:", age * 365)
    print("Age in hours:", age * 365 * 24)
    print("Age in minutes:", age * 365 * 24 * 60)
    print("Years until 100:", 100 - age)

except ValueError:
    print("Invalid input.")