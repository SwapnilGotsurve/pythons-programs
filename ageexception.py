# Create a user-defined exception class
class AgeException(Exception):
    pass

# Function to check age
def check_age(age):
    if age < 18:
        raise AgeException("Age must be 18 or above!")
    else:
        print("You are eligible!")

# Taking input from user
try:
    age = int(input("Enter your age: "))
    check_age(age)
except AgeException as e:
    print("Error:", e)
except ValueError:
    print("Please enter a valid number!")
