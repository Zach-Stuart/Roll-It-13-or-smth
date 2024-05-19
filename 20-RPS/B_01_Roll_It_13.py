# check users enter yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not type a valid response.")


def instruction():
    print('''
    **** Instructions ****
    
    When life gives you lemons, don't make lemonade
    Make life take the lemons back
    Get mad
    I don't want your damn lemons, what am I supposed to do with these?
    Demand to see life's manager
    Make life rue the day it thought it could give Cave Johnson lemons
    Do you know who I am?
    I'm the man who's gonna burn your house down!
    With the lemons!
    I'm gonna get my engineers to invent a combustible lemon that burns your house down!
    
    
    ''')

# checks users enter an integer
# that is more than 13
def int_check():

    while True:

        error = "Please enter an integer that is 13 or more."

        try:
            my_num = int(input("Enter an integer: "))

            # checks if the number is 13 or more
            if my_num < 13:
                print(error)
            else:
                return my_num

        except ValueError:
            print(error)

# main routine
print()
print('Roll It 13')
print()

#   loop for testing

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

print("program")
