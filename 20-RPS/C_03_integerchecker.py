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
