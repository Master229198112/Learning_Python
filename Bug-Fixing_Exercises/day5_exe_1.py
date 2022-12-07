menu = ["pasta", "pizza", "salad"]

# The problem was user_choice being a string
# The string needed to be converted into an int
# The solution was to add int() below

user_choice = int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."
print(message)