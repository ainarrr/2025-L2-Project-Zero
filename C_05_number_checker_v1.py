# Functions go here
def num_check(question, num_type, exit_code=None):
    """Checks users enter integer / float that is more than
    zero (or the optional exit code)"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero"
        change_to = int

    else:
        error = "Oops - please enter a number more than zero"
        change_to = float

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == "exit_code":
            return response

        try:
            # Change the response to an integer and check that its more than zero
            response = int(response)

            if response > 0:
                return response

            else:
                print(error)
        except Valueerror:
            print(error)
