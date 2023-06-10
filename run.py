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
    data1 = int(input(len("Enter weight here:\n ")))
    print("now enter your height(numbers only in cms)")
    data2 = int(input("Enter the weight and height here:\n "))
    print(f"Your weight is : {data1}kgs and height is :{data2}cms ")




get_user_data()
