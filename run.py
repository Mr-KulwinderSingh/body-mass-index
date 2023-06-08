# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Welcome to the Body_Mass_Index!\n")
print("As per the modern life style, and living in the world of technology")
print("every person needs to know what category of BMI he is in\n")

start = input("To start please type yes\n ")

if start != "yes":
    quit()


def get_weightand_height():
    """
    Get the body weight and height from the user to calculate BMI
    """
    print("Great ! Please provide your body weight and height in the following format ")
    print("70, 175")
    values_str = input("Enter the weight and height here: ")
    print(f"Weight and height provided is {values_str}:") 

get_weightand_height()
