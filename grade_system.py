try:

    user_number = input("Please enter a Mark: ")
    user_mark = float(user_number)

except ValueError:

    print("Invalid input. Please enter a valid number.")

else:

    if user_mark == 0:
        user_mark = 0

    if user_mark < 0 or user_mark > 100:
        print("Enter Valid Number (0 to 100)")
    else:

        print(f"Your Mark is : {user_mark:g}")

        if user_mark >= 90:
            print("Your Grade is: A")
        elif user_mark >= 80:
            print("Your Grade is: B")
        elif user_mark >= 70:
            print("Your Grade is: C")
        elif user_mark >= 60:
            print("Your Grade is: D")
        else:
            print("Your Grade is: E")