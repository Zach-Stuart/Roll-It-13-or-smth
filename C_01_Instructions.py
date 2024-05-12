print("Roll It 13")

#loop for testing

while True:
    want_instructions = input("Do you want to read the instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("You chose 'Yes'.")
    elif want_instructions == "no" or want_instructions == "n":
        print("You chose 'No'.")
    else:
        print("You did not choose a valid response.")