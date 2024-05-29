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


def instruction():
    print('''
    **** Instructions ****
    
    Pick between Rock, Paper and Scissors
    Do I really need to explain this to you
    Who hasn't played Rock, Paper, Scissors at some point in their life
    
    
    ''')


# main routine
print()
print('Roll It 13')
print()

#   loop for testing

want_instructions = string_checker("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

print("program")
