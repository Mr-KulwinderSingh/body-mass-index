# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Welcome to the Body_Mass_Index!\n")
print("As per the modern life style, and living in the world of technology")
print("every person needs to know what category of BMI he is in\n")

start = input("To start please type yes\n ")

if start.lower() != "yes":
    quit()


def get_weight_and_height():
    """
    Get the body weight and height from the user to calculate BMI
    """
    print("Great ! Please provide your body weight and height in the following format ")
    print("70, 175")

    user_values_str = input("Enter the weight and height here:\n ")
    user_data = user_values_str.split(", ")
    validate_data(user_data) 


def validate_data(values):
    """
    Converts all string values into integers, raises ValueError
    if strings cannot be converted to integers and if data provided
    is another format, all done by try statement
    """

    try:
        if len(values) != 2:
            raise ValueError(
            f"exactly 2 value required, you provided {len(values)}"
        )
    except ValueError as e:
        print(f"Provided Credentials are invalid: {e}, please try again\n ")


get_weight_and_height()
