# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid response from the following list: {valid_ans}"

    while True:

        # make sure user response is lowercase
        user_response = input(question).lower()
        for item in valid_ans:
            # check if user response is a word in the list
            if item == user_response:
                return item

            # check if user response is same as first letter of an item in list
            elif user_response == item[0]:
                return item

        # print error if user enters invalid response
        print(error)
        print()


# main routine

rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want to read the instructions?")

print("You chose: ", want_instructions)

user_choice = string_checker("Choose: ", rps_list)
print("You chose: ", user_choice)