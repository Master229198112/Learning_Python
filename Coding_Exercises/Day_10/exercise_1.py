try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter Value: "))
    if total_value == 0:
        exit("Your total value cannot be zero")

    percentage = (value / total_value) * 100
    print(f"This is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the code again")

# Another way for same output.
#
# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#
#     percentage = value / total_value * 100
#     print(f"That is {percentage}%")
# except ValueError:
#     print("You need to enter a number. Run the program again.")
# except ZeroDivisionError:
#     print("Your total value cannot be zero.")
