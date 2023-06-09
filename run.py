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
    print("Please provide your body weight(numbers only in kgs)")
    data1_str = int(input("Enter weight here:\n "))
    print("now enter your height(numbers only in cms)")
    data2_str = int(input("Enter the weight and height here:\n "))
    print(f"Weight and height provided are {data1_str, data2_str}")

    data1_str=data2_str = user_data
    validate_data(user_data) 


def validate_data(values):
    """
    Converts all string values into integers, raises ValueError
    if strings cannot be converted to integers and if data provided
    is another format, all done by try statement
    """

    try:
        [int(value) for value in values]
        if len(values) != 3:
            print(f"Please enter valid numbers")
    except ValueError as e:
        print(f"Enter only numbers please: {e}, please try again.\n")


  

get_user_data()
