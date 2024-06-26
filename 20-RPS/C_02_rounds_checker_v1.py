# this code is a fixed version generated by chatgpt

def int_check(to_check):
    while True:
        error = "Please enter an integer that is 1 or more."

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks if the number is 1 or more
            if response < 1:
                return "invalid"
            else:
                return response

        except ValueError:
            return "invalid"


# Automated testing is below in the form (test_case, expected_value)
to_check = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    ('1', 1),
    ('2', 2),
    ('', 'infinite'),
]

# run tests!
for item in to_check:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_check(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
