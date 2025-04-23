while True:
    try:
        user_input = int(input("Enter an integer: "))
        print(f"You entered the integer: {user_input}")
        break
    except ValueError:
        print("Error: That is not a valid integer. Please try again.")