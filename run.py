# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
    print("Please provide your body weight(in kgs)")
    name = input("Please enter your name:\n")
    data1 = int(input("Enter your weight here:\n "))
    print("now enter your height(only in cms)")
    data2 = int(input("Enter the height here:\n "))
    print(f"Your weight is : {data1}kgs and height is :{data2}cms ")

    calculate_bmi(name, data1, data2)



def calculate_bmi(name, data1, data2):
    height = data2 / 100
    bmi = data1 / (height ** 2) 
    if bmi < 25:
        print(name + "You have a good body weight :)")
    else:
        print(name + "I'm sorry your wight is bit high")

    


get_user_data()

