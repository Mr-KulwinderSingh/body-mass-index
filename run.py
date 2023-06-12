# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import math

print("Welcome to the Body_Mass_Index!\n")
print("As per the modern life style, and living in the world of technology")
print("every person needs to know what category of BMI he is in\n")

start = input("To start please type yes\n ")

if start.lower() != "yes":
    quit()


def get_user_data():
    """
    Get the body weight and height from the user to calculate BMI
    """
    
    print("Great !")
    name = input("Please enter your name:\n")
    print("Please provide your body weight(in kgs)")

    age = int(input("Please enter your age:\n"))
    print(age)
    
    data1 = int(input("Enter your weight here:\n "))
    print("now enter your height(only in cms)")
    data2 = int(input("Enter the height here:\n "))
    print(f"Your weight is : {data1}kgs and height is :{data2}cms\n")


    weight = data1 
    height = data2
    user_age = age 
    
    validate_input(weight, height, user_age)

def validate_input(weight, height, user_age):
    """
    Inside the try, it converts all string values to integers,
    raises the ValueError if string cannot be converted to
    integers, or there aren't exact values as per requirement 
    """
    try:
        if user_age < 2:
            raise ValueError(
                f"Sorry age should be above 2 years you provided {user_age}"
            )
        elif user_age > 100:
            raise ValueError(
                f"Sorry max age to calculate BMI is 100 your age {user_age}"
            )
    except ValueError as e:
            print(f"Invalid entry: {e}, please try again.\n ")


def calculate_bmi(name, data1, data2):
    """
    It calculate the BMI from data received from get user data
    function and produce the required result, it also tells
    the user if their wieght is good or hight as per BMI
    calculations
    """ 
    height = data2 / 100
    bmi = data1 / (height ** 2) 
    result = round(bmi,2)
    print(f"Hey " + name +" "+ "your BMI is:", result)

    if result < 25:
        print( name + " " + "You have a good weight according to BMI:)\n")
    else:
        print(name + " " + "sorry but your weight is a bit high\n")

    


get_user_data()




