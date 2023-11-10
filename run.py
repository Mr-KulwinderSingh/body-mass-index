from pyfiglet import figlet_format

import math

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

figlet_format("BODY MASS INDEX", font="small")

print(figlet_format("BODY MASS INDEX", font="small"))


def get_user_data():
    """
    This function starts the whole process of the BMI app with the
    welcome message & info about exception and rare statement for the
    user. It appeals the user to follow the prompts. Get user data
    (name, age, body weight and height) from the user to calculate
    BMI. Runs a while loop to collect the valid data appropriate
    to the required age, the loop will be keep requesting until the
    given data is valid.
    """
    print("            Welcome to the Body_Mass_Index!\n")
    print("----------This BMI is for the age 16yrs to 100yrs ------------ ")
    print("--------------------------------------------------------------- ")
    print("Our modern eat-out style, and living in the world of technology")
    print("every person needs to know what category of BMI he/she is in\n")

    print("-------------***** Exceptions and Rare *****--------------------")
    print("----------------------------------------------------------------")
    print("Adult women and men weighing 100kg who are between 201.0cm and")
    print("219.0 cm tall are considered to be of a healthy weight as measured")
    print("by body mass index (bmi),but our BMI is restricted to 200cm height")
    print("----------------------------------------------------------------")
    print("This BMI calculator has limits i.e. it can take the age of the ")
    print(" 16 years to 100 years and weight 40kgs to 100kgs plus the height")
    print("restrictions upto 200cm, please consider them before entering your")
    print(".                   details! Good Luck! \n")

    start = input("To start using the BMI app please type yes:\n ")

    while start.lower() != "yes":
        print(
            Fore.RED + f"In order to start the app, user has to type yes!\n ")
        start = input("To start please type yes:\n ")
        print(f"You said {start} to start")

    user1_name = input("Enter your name:\n")
    while user1_name.strip() == "" or not user1_name.isalpha(
    ) or (len(user1_name) <= 2) or (len(user1_name) >= 12):
        print(
            Fore.RED + "Username should be 3 to 12 characters only.")
        user1_name = input("Enter your name:\n")

    print(f'Hello {user1_name}')
    while True:

        user1_age = input("Enter your Age (a whole number only):\n")
        while not user1_age.isdigit():
            print(
                Fore.RED +
                " User age is required, enter a valid age(a whole number)")
            user1_age = input("Enter your Age (a whole number only):\n")

        user1_weight = input(
            "Enter your Weight(in kgs only, decimal not allowed):\n")
        while not user1_weight.isdigit():
            print(
                Fore.RED + "Weight is required, (a whole number only)")
            user1_weight = input(
                "Enter your Weight(in kgs only, decimal not allowed):\n")

        user1_height = input(
            "Enter your Height(in cms only, decimal not allowed):\n")
        while not user1_height.isdigit():
            print(
                Fore.RED + "User height is required, (a whole number only)")
            user1_height = input(
                "Enter your Height(in cms only, decimal not allowed):\n")
    # while True:

        class User:
            """
            Class User helps to manipulate and represent data in the form it
            has to be in the terminal, it correspond with the main function,
            takes the user input and segregate accordingly

            """

            def __init__(self, name, user_age, weight, height):
                self.name = name
                self.user_age = user_age
                self.weight = weight
                self.height = height

            def another(self):
                print(Fore.YELLOW + f"Your name is {self.name}\n")
                print(Fore.YELLOW + f"You are {self.user_age} years old\n")
                print(Fore.YELLOW + f"Your weight is {self.weight}kgs\n")
                print(Fore.YELLOW + f"Your height is {self.height}cms\n")

        display_user = User(user1_name, user1_age, user1_weight, user1_height)
        display_user.another()
        weight = int(float(user1_weight))
        height = int(float(user1_height))
        user_age = int(float(user1_age))

        calculate_bmi(user1_name, weight, height)

        validate_user_weight(weight)
        validate_user_height(height)

        if validate_user_age(user_age):
            print("Thanks for using BMI Calculator App!\n ")
            break
        elif validate_user_weight(weight):
            print("Thanks for using BMI Calculator App!\n ")
            break
        elif validate_user_height(height):
            print("Thanks for using BMI Calculator App!\n ")
            break
    return user1_name, weight, height, user_age
    print(user1_name, weight, height, user_age)


def validate_user_age(user_age):
    """
    This function checks if the user enters an integer or not,
    plus it also checks the error if the provided age range is
    valid and if it's not valid value error will be triggered,
    any other exception will detected here and informed to the
    user
    """
    try:
        if user_age < 16 or user_age > 100:
            raise ValueError(
                Fore.RED + f"Correct user age in order to calculate BMI"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again.\n ")
        return False

    return True


def validate_user_weight(weight):
    """
    Inside the try, this function checks if the user enters an integer
    or not, plus it also checks an error if the provided weight range is
    valid & if it's not valid as per the BMI valid weight range,value error
    will be triggered, empty or blank space can also be detected here
    in this validation function
    """
    try:

        if weight < 40 or weight > 120:
            raise ValueError(
                Fore.RED + f"Sorry Invalid weight range entered: {weight}"
            )
    except ValueError as e:
        print(f"Invalid entry: {e}, please try again.\n ")
        return False
    return True


def validate_user_height(height):
    """
    Inside the try, this function checks if the user enters an integer
    or not, plus it also gives an error if the provided height range is
    valid and if it's not valid as per the BMI valid height range error
    will be triggered, empty or blank space can also be detected here
    in in this validation function
    """

    try:

        if height < 80 or height > 200:
            raise ValueError(
                Fore.RED + f"Sorry Invalid height range entered:{height}"
            )
    except ValueError as e:
        print(f"Invalid entry:{e}, please try again.\n ")
        return False
    return True


def calculate_bmi(name, weight, height):
    """
    It calculates the BMI of the data received from the user
    and generates the required result, it also tells
    the user if their wieght is good or high as per BMI
    calculations
    """

    height = height / 100
    bmi = weight / (height ** 2)
    result = round(bmi, 2)
    print('\033[32m'f"Hey " + name + " " + "your BMI is:", result)

    if result < 25:
        print(Fore.GREEN + name + " " + "Your weight is good as per BMI:)\n")
    else:
        print(Fore.RED + name + " " + "sorry but your weight is a bit high\n")


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
