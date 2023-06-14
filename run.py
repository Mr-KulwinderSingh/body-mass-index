# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import math

import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset= True)



print("Welcome to the Body_Mass_Index!\n")
print("As per the modern life style, and living in the world of technology")
print("every person needs to know what category of BMI he is in\n")

print("-------------***** Exceptions and Rare *****--------------------")
print("----------------------------------------------------------------")
print("Adult women and men weighing 100kg who are between 201.0cm and ")
print("219.0 cm tall are considered to be of a healthy weight as measured")
print("by body mass index (bmi)2, but this BMI is restricted to 200cm height")
print("----------------------------------------------------------------")
print("This BMI calculator has limits i.e. it can take the age of the user")
print("from 2 years to 100 years and weight 5 kgs to 100 kgs plus the height")
print("restrictions upto 200cm, please consider them before entering")
print("your details! Good Luck! \n")

start = input("To start please type yes:\n ")



if start.lower() != "yes":
    quit()




def get_user_data():
    """
    Get the user data (name, age, body weight and height) from the
    user to calculate BMI. Run a while loop to collect the valid 
    data appropriate to the required age, the loop will be keep 
    requesting until the given data is valid.
    """

    while True:
    
        print("Great !")
        name = input("Please enter your name:\n")
        
        age = int(input("Please enter your age:\n"))
        
        print("Please provide your body weight(in kgs)")
        data1 = int(input("Enter your weight here:\n "))

        print("now enter your height(only in cms)")
        data2 = int(input("Enter the height here:\n "))
        print(f"Your weight is : {data1}kgs and height is :{data2}cms\n")


        weight = data1 
        height = data2
        user_age = age
        
        calculate_bmi(name, weight, height)


        if validate_input(weight, height, user_age):
            print("Given entries are valid!")
            break
        
    return name, weight, height, user_age

def validate_input(weight, height, user_age):
    """
    Inside the try, it converts all string values to integers,
    raises the ValueError if string cannot be converted to
    integers, or there aren't exact values as per requirement 
    """
    try:
        if user_age < 5:
            raise ValueError(
                f"Sorry age should be above 2 years you provided {user_age}"
            )
        elif user_age > 100:
            raise ValueError(
                f"Sorry max age to calculate BMI is 100 your age {user_age}"
            )
        elif weight < 5:
            raise ValueError(
                f"Sorry weight should be a valid number you provided {weight}"
            )
        elif weight > 120:
            raise ValueError(
                f"Sorry weight should be a valid number you provided {weight}"
            )
        elif height > 200:
            raise ValueError(
                f"Sorry above 200cm height is rare and can be unreal you entered: {height}"
            )
    except ValueError as e:
            print(f"Invalid entry: {e}, please try again.\n ")
            return False

    return True



def calculate_bmi(name, weight, height):
    """
    It calculates the BMI of the data received from the user. 
    and generates the required result, it also tells
    the user if their wieght is good or high as per BMI
    calculations
    """ 
   
    height = height / 100
    bmi = weight / (height ** 2) 
    result = round(bmi,2)
    print('\033[32m'f"Hey " + name +" "+ "your BMI is:", result)

    if result < 25:
        print('\033[32m'+ name + " " + "You have a good weight according to BMI:)\n")
    else:
        print('\033[31m' + name + " " + "sorry but your weight is a bit high\n")


def main():
    """
    Runs all the functions in the programme
    """

    name, user_age, weight, height = get_user_data()

    choice_to_restart = input('Press any key to restart or "q" to quit\n ')

    if choice_to_restart == "q":
        (quit)

    else:

        main()



main()




